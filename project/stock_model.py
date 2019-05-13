import pandas as pd
import numpy as np
import warnings
from keras import models
from keras import layers


class StockModel:
    def __init__(self, stock_data="__DEFAULT__", look_back=30, verbose=False):
        self.model = models.Sequential()

        if stock_data == '__DEFAULT__':
            def_data = pd.read_csv("compiled_data.zip", error_bad_lines=False, index_col="Date", parse_dates=True)
            def_data = def_data.drop(columns='Unnamed: 0')
            self.stock_data = def_data
        else:
            self.stock_data = stock_data

        self.look_back = look_back
        self.x_train_raw = pd.DataFrame()
        self.x_test_raw = pd.DataFrame()
        self.x_train = []
        self.y_train = []
        self.data_size = 0
        self.verbose = verbose

        if self.verbose:
            print("===Initialized StockModel===")
            print("\tLooking back %d days." % self.look_back)

    def select_stock(self, ticker):
        is_ticker = self.stock_data['ticker'] == str.upper(ticker)
        selected_stock = self.stock_data[is_ticker]
        if selected_stock.empty:
            warnings.warn("Could not find any stock matching ticker %s" % ticker)
        if self.verbose:
            print("\tSelected Stock %s" % ticker)
            print(selected_stock.describe())
        return selected_stock

    def prep_data(self, stock_df, stock_feature='Close'):
        frame_split = int(round(len(stock_df.index) * (4 / 5)))
        training_data = pd.DataFrame(stock_df[stock_feature])

        self.x_train_raw = training_data.iloc[:frame_split]
        self.x_test_raw = training_data.iloc[frame_split:frame_split + self.look_back * 2]
        self.data_size = self.x_train_raw.shape[0]

        if self.verbose:
            print("Prepared Data using feature \"%s\"." % stock_feature)
            print(self.x_train_raw.tail())

    def build_model(self, epochs=5, batch_size=32):
        x_train_np = np.array(self.x_train_raw)

        for i in range(self.look_back, self.data_size):
            self.x_train.append(x_train_np[i - self.look_back:i, 0])
            self.y_train.append(x_train_np[i, 0])

        self.x_train, self.y_train = np.array(self.x_train), np.array(self.y_train)
        self.x_train = np.reshape(self.x_train, (self.x_train.shape[0], self.x_train.shape[1], 1))

        #  LSTM Networks are repeatedly referred to as the best option for forward-looking predictions on Stocks
        #  See: - https://en.wikipedia.org/wiki/Long_short-term_memory
        #       - https://github.com/DarkKnight1991/Stock-Price-Prediction
        self.model.add(layers.LSTM(units=100, return_sequences=True, input_shape=(self.x_train.shape[1], 1)))
        self.model.add(layers.LSTM(units=75, return_sequences=True))
        self.model.add(layers.LSTM(units=50))
        # I chose to normalize the data at this point, given how many inputs there are in the form of stock data (
        # usually >1000!)
        self.model.add(layers.BatchNormalization())
        # This single output node should reflect a predicted price for Date(N) based on the previous LOOK_BACK number of
        # datapoints.
        self.model.add(layers.Dense(units=1))
        # Now compile and train
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.model.fit(self.x_train, self.y_train, epochs=epochs, batch_size=batch_size)

    def predict_on_data(self):
        test_data_size = self.x_test_raw.shape[0]

        combined_total = pd.concat((self.x_train_raw, self.x_test_raw), axis=0)
        validation_data = combined_total[combined_total.shape[0] - test_data_size - self.look_back:].values

        x_test = []

        for i in range(self.look_back, test_data_size):
            x_test.append(validation_data[i - self.look_back:i, 0])

        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

        return self.model.predict(x_test)

    @property
    def testing_values(self):
        return self.x_test_raw.values

    @property
    def training_values(self):
        return self.x_train_raw.values
