from src.data_sources.yahoo import YahooFinance
from src.model.tables import Company
from src.database.connection import Session

import aiohttp
import asyncio
from yahooquery import Ticker
import platform
from bs4 import BeautifulSoup
import requests as req

yf = YahooFinance()
company = Company()

with Session() as session:
    data = session.query(Company.ticker)
