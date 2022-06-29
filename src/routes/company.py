import json
from sqlalchemy import select
import pandas as pd
from flask import Blueprint
from markupsafe import escape

from src.database.connection import Session
from src.model.tables import Company

company = Blueprint('company', __name__)
session = Session()


@company.route('/company/<ticker>', methods=['GET', 'POST'])
def getTicker(ticker):
    ticker = ticker.upper()
    try:
        stmt = select(Company).where(Company.ticker == ticker)
        data = session.execute(stmt)
    except Exception as exception:
        print(f"Getting {ticker} from the database failed. {exception} ")
        session.rollback()
    result = {}
    for obj in data.scalars():
        result[obj.ticker] = {'name': obj.name, 'description': obj.description, 'country': obj.country,
                              'sector': obj.sector, 'industry': obj.industry, 'exchange': obj.exchange}
    return result
