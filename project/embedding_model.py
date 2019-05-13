import pandas as pd
import numpy as np
from keras import models
from keras import layers

LOOK_BACK = 500

# Data complied using stock_data_frame_builder.py
stock_data = pd.read_csv("compiled_data.zip", error_bad_lines=False, index_col="Date", parse_dates=True)
stock_data = stock_data.drop(columns='Unnamed: 0')  # Result of how to_csv saved the data.


def select_stock(stock_ticker):
    is_ticker = stock_data['ticker'] == stock_ticker
    selected_stock = stock_data[is_ticker]

    return selected_stock


def prep_stock_data(stock_df, stock_feature='Close'):
    frame_split = int(round(len(stock_df.index) * (4 / 5)))

    training_data = stock_df[stock_feature]
    training_data = pd.DataFrame(training_data)

    train_raw = training_data.iloc[:frame_split]
    test_raw = training_data.iloc[frame_split:frame_split + LOOK_BACK * 2]  # This was found by trial and error

    prepared_data = {
        'x_train': train_raw,
        'x_test': test_raw
    }
    return prepared_data


def predict_on_data(dict_of_data, keras_model):
    train_raw = dict_of_data['x_train']
    test_raw = dict_of_data['x_test']

    test_data_size = test_raw.shape[0]

    combined_total = pd.concat((train_raw, test_raw), axis=0)
    validation_data = combined_total[combined_total.shape[0] - test_data_size - LOOK_BACK:].values

    x_test = []

    for i in range(LOOK_BACK, test_data_size):
        x_test.append(validation_data[i - LOOK_BACK:i, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    return keras_model.predict(x_test)


apple_stock = select_stock('AAPL')
apple_stock.describe()

converted_stock_data = prep_stock_data(apple_stock)
x_train_raw = converted_stock_data['x_train']
x_test_raw = converted_stock_data['x_test']

data_size = x_train_raw.shape[0]

# MARK: - Model Training
x_train_np = np.array(x_train_raw)

x_train = []
y_train = []

for i in range(LOOK_BACK, data_size):
    x_train.append(x_train_np[i - LOOK_BACK:i, 0])
    y_train.append(x_train_np[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

model = models.Sequential()

#  LSTM Networks are repeatedly referred to as the best option for forward-looking predictions on Stocks
#  See: - https://en.wikipedia.org/wiki/Long_short-term_memory
#       - https://github.com/DarkKnight1991/Stock-Price-Prediction

model.add(layers.LSTM(units=100, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(layers.LSTM(units=75, return_sequences=True))
model.add(layers.LSTM(units=50))

# I chose to normalize the data at this point, given how many inputs there are in the form of stock data (usually
# >1000!)
model.add(layers.BatchNormalization())

# This single output node should reflect a predicted price for Date(N) based on the previous LOOK_BACK number of
# datapoints.
model.add(layers.Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=5, batch_size=32)

predictions = predict_on_data(converted_stock_data, model)
predictions = pd.DataFrame(predictions)
predictions.info()
