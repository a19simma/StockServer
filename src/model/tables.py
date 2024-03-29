from sqlalchemy import DDL, Column, ForeignKey, event
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, TIMESTAMP, BIGINT
from pandas import DataFrame
from datetime import datetime, timedelta
from src.data_sources.yahoo import YahooFinance

from src.database.connection import engine

Base = declarative_base()


class Company(Base):
    __tablename__ = "company"
    ticker = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    exchange = Column(String)
    start = Column(TIMESTAMP)
    updated = Column(TIMESTAMP)
    currency = Column(String)

    def addDataFrame(self, data: DataFrame, session):
        for _, row in data.iterrows():
            entry = Company(ticker=row['ticker'],
                            name=row['name'],
                            exchange=row['exchange'],
                            start=row['start'],
                            updated=datetime.now(),
                            currency=row['currency'])

            try:
                session.add(entry)
                session.commit()
            except Exception as e:
                print(f"{entry} already exists and can't be added again", e)
                session.rollback()


class StocksDaily(Base):
    __tablename__ = "stocks_daily"
    timestamp = Column(TIMESTAMP, primary_key=True)
    ticker = Column(String, ForeignKey(Company.ticker),
                    primary_key=True, index=True)
    open = Column(DOUBLE_PRECISION)
    high = Column(DOUBLE_PRECISION)
    low = Column(DOUBLE_PRECISION)
    close = Column(DOUBLE_PRECISION)
    volume = Column(BIGINT)

    def addDataFrame(self, data: DataFrame, session):
        for _, row in data.iterrows():
            entry = StocksDaily(timestamp=row['timestamp'],
                                ticker=row['ticker'],
                                open=row['open'],
                                high=row['high'],
                                low=row['low'],
                                close=row['close'],
                                volume=row['volume'])
            try:
                session.add(entry)
            except Exception as e:
                print(f"{entry} already exists and can't be added again", e)
                session.rollback()
        session.commit()


event.listen(
    StocksDaily.__table__, 'after_create', DDL(
        f"SELECT create_hypertable('{StocksDaily.__tablename__}', 'timestamp');")


)

Base.metadata.create_all(engine)
