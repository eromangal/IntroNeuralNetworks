import pandas_datareader.data as pdr
import fix_yahoo_finance as fix
import time
fix.pdr_override()


def get_stock_data(ticker, start_date, end_date):
    all_data = pdr.get_data_yahoo(ticker, start_date, end_date)
    stock_data = all_data["Adj Close"]
    stock_data.to_csv("stock_prices.csv")


def get_sp500(start_date, end_date):
    sp500_data = sp500_all_data["Adj Close"]
    sp500_data.to_csv("sp500_data.csv")


if __name__ == "__main__":
    get_stock_data("AAPL", "2018-05-01", "2018-06-01")
    # get_sp500("2018-05-01", "2018-06-01")
