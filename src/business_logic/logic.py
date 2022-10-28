from src.IO.import_data import *
from src.algo.algo import *

# def check_ticker(ticker):
#     result = get_SNP500(ticker)
#     return f'{result}\n'

def get_prediction(ticker):
    if get_SNP500(ticker) == ticker:
        df = get_last_stock_price(ticker, True)
        average = calculate(df)
        print(df['close'].iloc[-1], 'today')
        print(average, 'tomorrow')
        # if df['close'].iloc[-1:] == 'None':
        #     continue
        # else:
        return 'Sell' if df['close'].iloc[-1] > average else 'Buy'

    else:
        return get_SNP500(ticker)