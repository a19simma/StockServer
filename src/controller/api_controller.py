from pandas import DataFrame
from src.data_sources.yahoo import YahooFinance
from src.data_sources.alpha import AlphaVantage


class ApiController():
    def __init__(self):
        self.yahoo_api = YahooFinance()
        self.alpha_api = AlphaVantage()

    def getTicker(self, ticker: str, api='alpha') -> DataFrame:
        """Returns data of a specific ticker in the form of a pandas dataframe object."""
        if api == 'alpha':
            try:
                return self.alpha_api.getTicker(ticker)
            except Exception as error:
                print(error)

        try:
            return self.yahoo_api.getTicker(ticker)
        except Exception as error:
            print(error)

        raise Exception('No Api available for the request.')

    def getCompany(self, ticker: str, api='alpha') -> DataFrame:
        if api == 'alpha':
            try:
                return self.alpha_api.getCompany(ticker)
            except Exception as error:
                print(error)

        raise Exception('No Api available for the request.')
 