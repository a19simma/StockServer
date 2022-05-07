import yfinance as yf
from pandas import DataFrame


class YahooFinance():
    def getTicker(self, ticker: str) -> DataFrame:
        ticker_object = yf.Ticker(ticker)
        return ticker_object.history(period='max')
