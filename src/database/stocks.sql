CREATE TABLE public.stocks_intraday (
    "time" timestamp NOT NULL,
    symbol text NULL,
    price_open double precision NULL,
    price_close double precision NULL,
    price_low double precision NULL,
    price_high double precision NULL,
    trading_volume int NULL
);
CREATE EXTENSION IF NOT EXISTS timescaledb;
SELECT create_hypertable('stocks_intraday', 'time');