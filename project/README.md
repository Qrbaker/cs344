# StockModel: Using Keras to Predict Stock Performance
By Quentin Baker

This project uses Keras LSTM models, combined with Normalization layers, to predict a stock's performance.

## Installation
The primary `StockModel` class is written in Python 3, and has the following non-core dependecies:
* Pandas
* NumPy
* Keras
  * TensorFlow as Keras Backend
  
You can quickly install all requirements with `pip install -r requirements.txt`

The dataset is avalible here:
https://drive.google.com/file/d/1_jMe-hRv9GRdK1dF7zv992nHKJ71ktsj/view?usp=sharing

Just place the .zip file in the \project\ folder, don't extract it.
## Usage
Import the StockModel Class and Initialize a model:

    from stock_model import StockModel
    my_model = StockModel()

Select a stock based on its ticker:

    apple_stock = my_model.select_stock('AAPL')
 
Prep the data and build the model:

    my_model.prep_data(apple_stock)
    my_model.build_model(epochs=5)
    
    predictions = my_model.predict_on_data()

`predictions` Is now an array containing predictions of closing price data for AAPL.