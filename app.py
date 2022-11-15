from flask import Flask
from src.IO.import_data import *
from src.business_logic.logic import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/get_stock_val/<ticker>', methods=['GET'])
def get_stock_value(ticker):
    ticker = ticker.upper()  # Convert to uppercase to allow lowercase user input
    prediction = get_prediction(ticker, 'logistic_regression')
    return f'{prediction}\n'

if __name__ == '__main__':
    app.run()
