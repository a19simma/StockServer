from typing import Dict
from pandas import DataFrame
from sqlalchemy import BigInteger, DDL, Column, ForeignKey, MetaData, event, inspect, delete
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Date, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION

from src.database.connection import engine
from src.database.connection import Session

Base = declarative_base()
session = Session()


class Company(Base):
    __tablename__ = "company"
    ticker = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    country = Column(String)
    sector = Column(String)
    industry = Column(String)
    exchange = Column(String)


session.add(Company())


class StocksDaily(Base):
    __tablename__ = "stocks_daily"
    date = Column(Date, primary_key=True, index=True)
    ticker = Column(String, ForeignKey(Company.ticker), primary_key=True)
    open = Column(DOUBLE_PRECISION)
    high = Column(DOUBLE_PRECISION)
    low = Column(DOUBLE_PRECISION)
    close = Column(DOUBLE_PRECISION)
    volume = Column(BigInteger)


event.listen(
    StocksDaily.__table__, 'after_create', DDL(
        f"SELECT create_hypertable('{StocksDaily.__tablename__}', 'date');")
)

session.add(StocksDaily())
session.commit()
Base.metadata.create_all(engine)
