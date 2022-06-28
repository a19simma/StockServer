CREATE EXTENSION IF NOT EXISTS timescaledb;
CREATE TABLE public.stocks_daily (
    "date" DATE NOT NULL,
    ticker TEXT NOT NULL,
    "open" DOUBLE PRECISION NULL,
    high DOUBLE PRECISION NULL,
    low DOUBLE PRECISION NULL,
    "close" DOUBLE PRECISION NULL,
    volume INT NULL,
    PRIMARY KEY("date",ticker)
);
SELECT create_hypertable('stocks_daily', 'date');
CREATE INDEX ix_ticker_time ON stocks_daily (ticker,date DESC);

CREATE TABLE company (
    ticker TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT,
    country TEXT,
    sector TEXT,
    industry TEXT,
    exchange TEXT  
);
CREATE INDEX ix_ticker_name ON company (ticker,name DESC);