import requests as req
from bs4 import BeautifulSoup
import pandas as pd
import asyncio
from datetime import datetime

from src.database.connection import Session
from src.model.tables import Company, StocksDaily
from src.data_sources.yahoo import YahooFinance

if __name__ == '__main__':
    """This module populates tickers from the OMX30 and SP500 indexes, it is meant as a means to 
    add test data to the database initially. It takes a long time to fetch all the ~4.5m rows from Yahoo,
    be patient."""

    OMX30 = [
        'ABB.ST',
        'ALFA.ST',
        'ALIV-SDB.ST',
        'ASSA-B.ST',
        'ATCO-A.ST',
        'ATCO-B.ST',
        'AZN.ST',
        'BOL.ST',
        'ELUX-B.ST',
        'ERIC-B.ST',
        'ESSITY-B.ST',
        'EVO.ST',
        'GETI-B.ST',
        'HEXA-B.ST',
        'HM-B.ST',
        'INVE-B.ST',
        'KINV-B.ST',
        'NDA-SE.ST',
        'SAND.ST',
        'SCA-B.ST',
        'SEB-A.ST',
        'SHB-A.ST',
        'SINCH.ST',
        'SKA-B.ST',
        'SKF-B.ST',
        'SWED-A.ST',
        'SWMA.ST',
        'TEL2-B.ST',
        'TELIA.ST',
        'VOLV-B.ST',
    ]

    async def addCompany(list):
        for str in list:
            company = await yf.getCompany(str)
            company_table.addDataFrame(company, session)
            start = pd.to_datetime(company['start'].values[0])
            start = start - datetime.fromtimestamp(0)
            start = int(start.total_seconds())
            await addStock(str, start)

    async def addStock(str, start):
        history = await yf.getTicker(str, start, datetime.now())
        stocks_daily_table.addDataFrame(history, session)
        print(f'{str} added')

    yf = YahooFinance()
    company_table = Company()
    stocks_daily_table = StocksDaily()
    session = Session()
    tasks = []

    asyncio.run(addCompany(OMX30))

    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    page = req.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list = soup.find_all('tr')
    SP500 = [list[i].td.a.text for i in range(
        1, 501) if list[i].td is not None]
    SP500 = [e.replace(".", "-") for e in SP500]

    asyncio.run(addCompany(SP500))
