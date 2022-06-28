import os
from datetime import date
from dotenv import load_dotenv
from pandas import DataFrame
from polygon import RESTClient


class Polygon():
    def __init__(self):
        load_dotenv()
        key = os.getenv('POLYGON_API_KEY')
        self.api = RESTClient(api_key=key)

    def getTicker(self, ticker: str) -> DataFrame:
        data = self.api.get_aggs(
            ticker, 1, 'day',  date(1990, 1, 1), date.today())
        return DataFrame(data)

    def getCompany(self, ticker: str) -> DataFrame:
        pass


polygon = Polygon()
print(polygon.getTicker('MSFT'))
