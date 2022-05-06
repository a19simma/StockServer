from src.database.connection import connection, cursor
from src.data_sources.yahoo import YahooFinance

yahoo_api = YahooFinance()
msft = yahoo_api.getTicker('MSFT')

print(msft.describe())