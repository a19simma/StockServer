from datetime import datetime, timedelta
import pandas as pd
import asyncio

from src.model.tables import Company, StocksDaily
from src.database.connection import Session
from src.data_sources.yahoo import YahooFinance


async def updateTicker(ticker, updated, now):
    data = await yf.getTicker(ticker, round(updated.timestamp()), round(now))
    session.query(Company)\
        .filter(Company.ticker == ticker)\
        .update({Company.updated: datetime.fromtimestamp(now)}, synchronize_session=False)
    return data


if __name__ == '__main__':
    yf = YahooFinance()
    with Session() as session:
        tickers = session.query(Company.ticker, Company.updated).all()
        now = datetime.now().timestamp()
        data = []
        for ticker, updated in tickers:
            if datetime.now() - updated > timedelta(hours=18):
                ticker = asyncio.run(updateTicker(
                    ticker, updated, now))
                data.append(ticker)
        data = pd.concat(data)
        stocksdaily = StocksDaily()
        stocksdaily.addDataFrame(data, session)
        session.commit()
