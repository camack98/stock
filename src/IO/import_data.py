from datetime import datetime, timedelta

from yahoo_fin import stock_info as si


def get_last_stock_price(ticker, last=False):
    if last:
        now = datetime.now()
        start_date = now - timedelta(days=60)
        return si.get_data(ticker, start_date)
    return si.get_data(ticker)

def get_SNP500(ticker):
    if ticker not in si.tickers_sp500():
        return 'Ticker not in S&P500, please try again.'
    return ticker

print(get_last_stock_price('AAPL', True))