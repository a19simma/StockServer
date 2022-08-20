
from pandas import DataFrame
import aiohttp
import asyncio
import platform
from datetime import datetime, timedelta


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

    def formatURL(self, url: str, ticker: str, start, end):
        today = int(datetime.now().timestamp())
        result = f'{url}{ticker}?period1={start}&period2={today}&interval=1d'
        return result

    async def getTicker(self, tickers: list, start, end) -> DataFrame:
        data = []
        if isinstance(tickers, str):
            tickers = [tickers]
        for ticker in tickers:
            url = self.formatURL(self.history_url, ticker, start, end)
            result = await self.get(url)
            for i in range(0, len(result['chart']['result'][0]['timestamp'])):
                data.append({'timestamp': datetime.fromtimestamp(0) + timedelta(seconds=(result['chart']['result'][0]['timestamp'][i])),
                            'ticker': ticker,
                             'volume': result['chart']['result'][0]['indicators']['quote'][0]['volume'][i],
                             'open': result['chart']['result'][0]['indicators']['quote'][0]['open'][i],
                             'low': result['chart']['result'][0]['indicators']['quote'][0]['low'][i],
                             'close': result['chart']['result'][0]['indicators']['quote'][0]['close'][i],
                             'high': result['chart']['result'][0]['indicators']['quote'][0]['high'][i]})
        data = DataFrame(data)
        data = data.dropna()
        return data

    async def getCompany(self, ticker) -> DataFrame:
        data = []
        if isinstance(ticker, str):
            ticker = [ticker]
        url = f'{self.url}?symbols={",".join(ticker).strip()}'
        result = await self.get(url)

        for ticker in result['quoteResponse']['result']:
            data.append({
                'ticker': ticker['symbol'],
                'name': ticker['longName'],
                'exchange': ticker['fullExchangeName'],
                'start': datetime.fromtimestamp(0) + timedelta(seconds=(ticker['firstTradeDateMilliseconds']/1000)),
                'currency': ticker['currency']
            })
        data = DataFrame(data)
        data = data.dropna()
        return data
