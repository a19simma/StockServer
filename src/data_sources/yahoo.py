import yfinance as yf
from pandas import DataFrame


class YahooFinance():
    def getTicker(self, ticker: str) -> DataFrame:
        ticker_object = yf.Ticker(ticker)
        data = DataFrame(ticker_object.history(period='max'))

        ticker_column = [str(ticker)] * len(data.index)
        data.insert(0, 'ticker', ticker_column)
        data.reset_index(inplace=True)
        data = data.drop(columns=['Dividends', 'Stock Splits'])
        data.columns = ['date', 'ticker', 'open',
                        'high', 'low', 'close', 'volume']
        data = data.dropna()
        return data

    def getCompany(self, ticker: str) -> DataFrame:
        ticker_object = yf.Ticker(ticker)
        data = ticker_object.get_info()
        data = [{
            'ticker': data.get('symbol'),
            'name': data.get('longName'),
            'description': data.get('longBusinessSummary'),
            'country': data.get('country'),
            'sector': data.get('sector'),
            'industry': data.get('industry'),
            'exchange': data.get('exchange'),
        }]
        data = DataFrame(data)
        data = data.dropna()
        return data
