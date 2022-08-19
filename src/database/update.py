from src.data_sources.yahoo import YahooFinance
from src.database.connection import Session
from src.model.tables import Company, StocksDaily

import aiohttp
import asyncio
from yahooquery import Ticker
import platform
from bs4 import BeautifulSoup
import requests as req

yf = YahooFinance

result = asyncio.run(yf.getCompany(['aapl']))
print(result)
