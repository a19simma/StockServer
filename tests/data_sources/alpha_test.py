from ...src.data_sources.alpha import AlphaVantage
import pandas as pd

def test_getTicker_type():
    av = AlphaVantage()
    data, meta_data = av.getTicker('MSFT')
    assert type(data) is pd.DataFrame and type(meta_data) is dict