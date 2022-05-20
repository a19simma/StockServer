from src.data_sources.alpha import AlphaVantage
import pandas as pd

av = AlphaVantage()


def test_getTicker_type():
    data = av.getTicker('MSFT')
    assert type(data) is pd.DataFrame


def test_getCompany():
    data = av.getCompany('MSFT')
    assert type(data) is pd.DataFrame and len(data.columns) is 7
