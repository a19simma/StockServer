from typing import List
from datetime import datetime

from psycopg2.extras import execute_values
from psycopg2.errors import UniqueViolation
from pandas import DataFrame

from src.database.connection import connection, cursor
from src.data_sources.alpha import AlphaVantage


class StocksDaily:
    def addTicker(self, ticker: str) -> None:
        av = AlphaVantage()
        df = av.getTicker(ticker)
        query = f"INSERT INTO public.stocks_daily VALUES %s"
        data = df.values.tolist()
        for r in data:
            r[0] = datetime.date(r[0])
        try:
            execute_values(cursor, query, data)
            connection.commit()
        except UniqueViolation as error:
            print(
                f"There was an error entering the values into the database: {error}")

    def getAllTickers(self) -> List:
        query = 'SELECT ticker FROM company;'
        cursor.execute(query)
        data = cursor.fetchall()
        df = DataFrame(data)
        return cursor.fetchall()

    def getByTicker(self, ticker) -> DataFrame:
        query = f'SELECT * FROM stocks_daily WHERE ticker={ticker};'
        cursor.execute(query)
        data = DataFrame(cursor.fetchall())
        return data

    def getByTicker(self, ticker, start, end):
        pass

    def removeTicker(self, ticker: str) -> None:
        pass

    def __sanitize_data():
        pass
