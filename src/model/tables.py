from sqlalchemy import BigInteger, DDL, Column, ForeignKey, MetaData, event
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Date, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from pandas import DataFrame

from src.database.connection import engine

Base = declarative_base()


class Company(Base):
    __tablename__ = "company"
    ticker = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    exchange = Column(String)
    start = Column(BigInteger)
    currency = Column(String)

    def addDataFrame(self, data: DataFrame, session):
        for _, row in data.iterrows():
            entry = Company(ticker=row['ticker'],
                            name=row['name'],
                            exchange=row['exchange'],
                            start=row['start'],
                            currency=row['currency'])
            session.add(entry)
        session.commit()


class StocksDaily(Base):
    __tablename__ = "stocks_daily"
    date = Column(Date, primary_key=True, index=True)
    ticker = Column(String, ForeignKey(Company.ticker),
                    primary_key=True, index=True)
    open = Column(DOUBLE_PRECISION)
    high = Column(DOUBLE_PRECISION)
    low = Column(DOUBLE_PRECISION)
    close = Column(DOUBLE_PRECISION)
    volume = Column(BigInteger)

    def addDataFrame(self, data: DataFrame, session):
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


event.listen(
    StocksDaily.__table__, 'after_create', DDL(
        f"SELECT create_hypertable('{StocksDaily.__tablename__}', 'date');")


)

Base.metadata.create_all(engine)
