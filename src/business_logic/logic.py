from src.IO.import_data import *
from src.algo.algo import *


# def check_ticker(ticker):
#     result = get_SNP500(ticker)
#     return f'{result}\n'

def get_prediction(ticker, model):
    if get_SNP500(ticker) == ticker:
        if model == '30_day_average':
            df = get_last_stock_price(ticker, True)
            pred_value = calc_30_day_avg(df)
            print(df['close'].iloc[-1], 'today')
            print(pred_value, 'tomorrow')
            return 'Sell' if df['close'].iloc[-1] > pred_value else 'Buy'

        if model == 'logistic_regression':
            df_train = get_stock_data(ticker)
            df_test = get_last_stock_price(ticker, True)
            pred_value = logistic_regression(df_train, df_test)
            return 'Sell' if pred_value == 0 else 'Buy'
        else:
            return 'Null'

    else:
        return get_SNP500(ticker)

# print(get_prediction('A', 'logistic_regression'))
