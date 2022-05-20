from psycopg2.extras import execute_values
from pandas import DataFrame

from src.database.connection import connection, cursor
from src.data_sources.alpha import AlphaVantage


class Company():
    def add(self, ticker: str) -> None:
        query = "INSERT INTO company VALUES %s;"
        av = AlphaVantage()
        data = av.getCompany(ticker)
        try:
            execute_values(cursor, query, data)
            connection.commit()
        except Exception as error:
            connection.rollback()
            print(
                f"There was an error entering the company into the database: {error}")

    def remove(self, ticker: str) -> None:
        query = "DELETE FROM company where ticker=%s;"
        data = (ticker,)
        try:
            cursor.execute(query, data)
            connection.commit()
        except Exception as error:
            connection.rollback()
            print(
                f"There was an error removing the company from the database: {error}")

    def get(self, ticker: str) -> DataFrame:
        query = f'SELECT * FROM company WHERE ticker=%s;'
        data = (ticker,)
        try:
            cursor.execute(query, data)
            result = DataFrame(cursor.fetchall())
            return result
        except Exception as error:
            connection.rollback()
            print(
                f"There was an error retrieving the values from the database: {error}")
