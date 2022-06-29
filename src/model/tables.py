from typing import Dict
from pandas import DataFrame
from sqlalchemy import BigInteger, DDL, Column, ForeignKey, event, inspect, delete
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Date, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION

from src.database.connection import engine
from src.database.connection import Session

Base = declarative_base()
session = Session()


class StocksDaily(Base):
    __tablename__ = "stocks_daily"
    date = Column(Date, primary_key=True, index=True)
    ticker = Column(String, ForeignKey('company.ticker'), primary_key=True)
    open = Column(DOUBLE_PRECISION)
    high = Column(DOUBLE_PRECISION)
    low = Column(DOUBLE_PRECISION)
    close = Column(DOUBLE_PRECISION)
    volume = Column(BigInteger)

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def addDataFrame(self, data: DataFrame):
        for _, row in data.iterrows():
            entry = StocksDaily(date=row['date'],
                                ticker=row['ticker'],
                                open=row['open'],
                                high=row['high'],
                                low=row['low'],
                                close=row['close'],
                                volume=row['volume'])
            session.add(entry)
        session.commit()

    def removeDataFrame(self, ticker: DataFrame):
        stmt = delete(self).where(self.ticker == ticker)
        session.execute(stmt)


event.listen(
    StocksDaily.__table__, 'after_create', DDL(
        f"SELECT create_hypertable('{StocksDaily.__tablename__}', 'date');")
)


class Company(Base):
    __tablename__ = "company"
    ticker = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    country = Column(String)
    sector = Column(String)
    industry = Column(String)
    exchange = Column(String)

    def toDict(self) -> Dict:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def addDataFrame(self, company: DataFrame):
        data = Company(ticker=company['ticker'].values[0],
                       name=company['name'].values[0],
                       description=company['description'].values[0],
                       country=company['country'].values[0],
                       sector=company['sector'].values[0],
                       industry=company['industry'].values[0],
                       exchange=company['exchange'].values[0])
        session.add(data)
        session.commit()

    def removeCompany(self, company: str):
        stmt = delete(self).where(self.ticker == company)
        session.execute(stmt)


Base.metadata.create_all(engine)
