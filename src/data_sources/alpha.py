import os

from dotenv import load_dotenv
from pandas import DataFrame
from alpha_vantage.timeseries import TimeSeries


class AlphaVantage():
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        self.ts = TimeSeries(key=api_key, output_format='pandas')

    def getTicker(self, ticker: str) -> DataFrame:
        data, _ = self.ts.get_daily(
            symbol=ticker, outputsize='full')
        ticker_column = [str(ticker)] * len(data.index)
        data.insert(0, 'ticker', ticker_column)
        data.reset_index(inplace=True)
        data.columns = ['date', 'ticker', 'open',
                        'high', 'low', 'close', 'volume']
        return data
