from src.models.stocks_daily import StocksDaily

table = StocksDaily()


def test_addTicker():
    try:
        table.addTicker('AAPL')
    except:
        assert False


def test_getTicker():
    pass


def test_removeTicker():
    pass
