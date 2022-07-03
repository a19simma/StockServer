from src.data_sources.yahoo import YahooFinance
import pandas as pd


def test_getTicker_type():
    yf = YahooFinance()
    msft = yf.getTicker('MSFT')
    assert type(msft) is pd.DataFrame


def test_getCompany():
    yf = YahooFinance()
    msft = yf.getCompany('MSFT')
    assert type(msft) is pd.DataFrame and len(msft.columns) is 7
