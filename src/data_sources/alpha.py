import os

from dotenv import load_dotenv
from pandas import DataFrame
from alpha_vantage import timeseries, fundamentaldata


class AlphaVantage():
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('ALPHAVANTAGE_API_KEY')
        self.ts = timeseries.TimeSeries(key=api_key, output_format='pandas')
        self.fd = fundamentaldata.FundamentalData(output_format='pandas')

    def getTicker(self, ticker: str) -> DataFrame:
        data, _ = self.ts.get_daily(
            symbol=ticker, outputsize='full')
        ticker_column = [str(ticker)] * len(data.index)
        data.insert(0, 'ticker', ticker_column)
        data.reset_index(inplace=True)
        data.columns = ['date', 'ticker', 'open',
                        'high', 'low', 'close', 'volume']
        return data

    def getCompany(self, ticker: str) -> DataFrame:
        data, _ = self.fd.get_company_overview(ticker)
        data = DataFrame(data=data[[
                         'Symbol', 'Name', 'Description', 'Country', 'Sector', 'Industry', 'Exchange']])
        return data
