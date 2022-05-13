from typing import List
from datetime import date, datetime

from psycopg2.extras import execute_values
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
            connection.close()
        except Exception as error:
            connection.rollback()
            print(
                f"There was an error entering the values into the database: {error}")

    def getTicker(self, ticker) -> DataFrame:
        query = f'SELECT * FROM stocks_daily WHERE ticker=%s;'
        data = ticker
        try:
            cursor.execute(query, data)
            result = DataFrame(cursor.fetchall())
            connection.close()
            return result
        except Exception as error:
            connection.rollback()
            print(
                f"There was an error retrieving the values from the database: {error}")

    def getTicker_period(self, ticker: str, start: date, end: date) -> DataFrame:
        query = f'SELECT * FROM stocks_daily WHERE ticker=%s AND date BETWEEN %s AND %s;'
        data = (ticker, start, end)
        try:
            cursor.execute(query, data)
            result = DataFrame(cursor.fetchall())
            connection.close()
            return result
        except Exception as error:
            connection.rollback()
            print(
                f"There was an error retrieving the values from the database: {error}")

    def removeTicker(self, ticker: str) -> None:
        query = f'DELETE FROM stocks_daily WHERE ticker=%s;'
        data = (ticker)
        try:
            cursor.execute(query, data)
            connection.commit()
            connection.close()
        except Exception as error:
            connection.rollback()
            print(
                f"There was an error retrieving the values from the database: {error}")

    def __sanitize_data():
        pass
