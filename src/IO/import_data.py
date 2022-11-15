from datetime import datetime, timedelta

from yahoo_fin import stock_info as si


def get_last_stock_price(ticker, last=False):
    if last:
        now = datetime.now()
        start_date = now - timedelta(days=60) # Need more than 30 days because there are fewer
        # business days than calendar days (not every calendar day is a day when stock market is open).
        return si.get_data(ticker, start_date)
    return si.get_data(ticker)

def get_stock_data(ticker):
    now = datetime.now()
    end_date = now - timedelta(days=1)
    return si.get_data(ticker, end_date=end_date)

def get_SNP500(ticker):
    if ticker not in si.tickers_sp500():
        return 'Ticker not in S&P500, please try again.'
    return ticker

# print(get_last_stock_price('AAPL', True))
print(get_stock_data('AAPL'))