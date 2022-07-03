from sqlalchemy import BigInteger, DDL, Column, ForeignKey, MetaData, event
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Date, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION

from src.database.connection import engine

Base = declarative_base()


class Company(Base):
    __tablename__ = "company"
    ticker = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    country = Column(String)
    sector = Column(String)
    industry = Column(String)
    exchange = Column(String)


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

Base.metadata.create_all(engine)
