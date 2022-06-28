from pandas import DataFrame
from src.controller.api_controller import ApiController

api_controller = ApiController()


def test_get_ticker_alpha():
    api_controller.getTicker('MSFT')


def test_get_ticker_yahoo():
    api_controller.getTicker('MSFT', api='yahoo')


def test_get_ticker_error():
    try:
        api_controller.getTicker(12145)
    except:
        assert True


def test_get_company_alpha():
    assert type(api_controller.getCompany('MSFT')) is DataFrame


def test_get_company_error():
    try:
        api_controller.getCompany(12145)
    except:
        assert True
