from yahooquery import Ticker
import yfinance as yf
from pandas import DataFrame

import aiohttp
import asyncio
import platform


class YahooFinance():
    def __init__(self):
        self.url = "https://query2.finance.yahoo.com/v7/finance/quote"
        self.history_url = "https://query2.finance.yahoo.com/v8/finance/chart/"
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())

    async def get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    async def getTicker(self, ticker: str) -> DataFrame:
        ticker_object = Ticker(ticker, asynchronous=True)
        data = ticker_object.history(period='max', interval='1d')
        data.reset_index(inplace=True)
        try:
            data = data.drop(columns=['dividends'])
        except:
            pass
            # Not every dataset has splits

        try:
            data = data.drop(columns=['adjclose'])
        except:
            pass
            # Not every dataset has splits

        try:
            data = data.drop(columns=['splits'])
        except:
            pass
            # Not every dataset has splits

        data.columns = ['ticker', 'date', 'open',
                        'volume', 'low', 'high', 'close']
        data = data.dropna()
        return data

    async def getCompany(self, ticker) -> DataFrame:
        data = []
        url = f'{self.url}?symbols={",".join(ticker).strip()}'
        result = await self.get(url)

        for ticker in result['quoteResponse']['result']:
            data.append({
                'ticker': ticker.get('symbol'),
                'name': ticker.get('longName'),
                'exchange': ticker.get('fullExchangeName'),
                'start': ticker.get('firstTradeDateMilliseconds'),
                'currency': ticker.get('currency')
            })
        data = DataFrame(data)
        data = data.dropna()
        return data
