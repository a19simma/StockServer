from dotenv import load_dotenv
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import os

class AlphaVantage():
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        self.ts = TimeSeries(key=api_key, output_format='pandas')
    def getTicker(self, ticker):
        data, meta_data = self.ts.get_intraday(symbol=ticker, interval='1min', outputsize='full')
        return data, meta_data