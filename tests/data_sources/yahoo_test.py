from src.data_sources.yahoo import YahooFinance
import pandas as pd


def test_getTicker_type():
    yf = YahooFinance()
    msft = yf.getTicker('MSFT')
    assert type(msft) is pd.DataFrame
