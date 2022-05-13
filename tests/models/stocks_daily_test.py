from datetime import date, timedelta
from src.models.stocks_daily import StocksDaily

table = StocksDaily()


def test_addTicker():
    try:
        table.removeTicker('AAPL')
        table.addTicker('AAPL')
    except:
        assert False


def test_getTicker():
    try:
        table.getTicker('AAPL')
    except:
        assert False


def test_getTicker_period():
    start = date.today()-timedelta(days=30)
    end = date.today()
    try:
        result = table.getTicker_period('AAPL', start, end)
        if result.shape[0] < 30:
            assert True
    except:
        assert False


def test_removeTicker():
    pass
