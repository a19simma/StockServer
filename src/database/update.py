from datetime import datetime, timedelta
import pandas as pd

from src.model.tables import Company
from src.database.connection import Session
from src.data_sources.yahoo import YahooFinance

if __name__ == '__main__':
    yf = YahooFinance()
    with Session() as session:
        tickers = session.query(Company.ticker, Company.updated).all()
        now = datetime.now()
        data = pd.DataFrame()
        for ticker, updated in tickers:
            if datetime.now() - updated > timedelta(hours=18):
                data.concat(yf.getTicker(ticker, updated, now),
                            ignore_index=True)
                session.query(Company)\
                    .filter(Company.ticker == ticker)\
                    .update(updated=now)\
                    .execution_options(synchronize_session="fetch")
        company = Company()
        company.addDataFrame(data, session)
