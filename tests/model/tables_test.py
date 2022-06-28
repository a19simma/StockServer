from src.model.tables import StocksDaily, Company
from src.database.connection import session


def test():
    daily_table = StocksDaily()
    company_table = Company()
