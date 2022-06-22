from src.data_sources.alpha import AlphaVantage
from pandas import DataFrame

av = AlphaVantage()


def test_getTicker_type():
    try:
        data = av.getTicker('MSFT')
        assert type(data) is DataFrame
    except ValueError:
        assert True
    except:
        assert False


def test_getCompany():
    try:
        data = av.getCompany('MSFT')
        assert type(data) is DataFrame and len(data.columns) is 7
    except ValueError:
        assert True
    except Exception as error:
        print(error)
        assert False
