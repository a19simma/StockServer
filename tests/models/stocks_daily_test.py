from datetime import date, timedelta
from src.models.stocks_daily import StocksDaily
import pandas as pd

table = StocksDaily()


def test_addTicker():
    try:
        table.removeTicker('AAPL')
        table.addTicker('AAPL')
    except:
        assert False


def test_addTicker_error():
    try:
        table.addTicker('AAPL')
        assert False
    except:
        assert True


def test_getTicker():
    try:
        result = table.getTicker('AAPL')
        assert True
    except:
        assert False


def test_getTicker_error():
    try:
        result = table.getTicker(1234)
    except:
        assert True


def test_getTicker_period():
    start = date.today()-timedelta(days=30)
    end = date.today()
    try:
        result = table.getTicker_period('AAPL', start, end)
        if result.shape[0] < 30:
            assert True
    except:
        assert False


def test_getTicker_period_error():
    start = date.today()
    end = date.today()
    try:
        result = table.getTicker_period(1234, start, end)
        assert False
    except:
        assert True


def test_removeTicker():
    try:
        table.removeTicker('AAPL')
        assert True
    except:
        assert False


def test_removeTicker_error():
    try:
        table.removeTicker(123)
        assert False
    except:
        assert True
