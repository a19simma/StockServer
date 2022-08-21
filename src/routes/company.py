import json
from sqlalchemy import select
import pandas as pd
from flask import Blueprint
from markupsafe import escape

from src.database.connection import Session
from src.model.tables import Company

company = Blueprint('company', __name__)


@company.route('/company', methods=['GET'])
def root():
    html = "<h1>This is the root of the company endpoint"
    html += "<p>Access the data of a specific company by its ticker eg. /company/MSFT"
    html += "<h2>Following is a list of companies:</h2>"
    html += "<ul>"

    with Session() as session:
        companies = session.execute(select(Company)).scalars()
        for company in companies:
            html += "<li><b>" + str(company.ticker) + \
                "</b>: " + str(company.name)
    return html


@company.route('/company/<ticker>', methods=['GET'])
def getTicker(ticker):
    ticker = ticker.upper()
    with Session() as session:
        try:
            stmt = select(Company).where(Company.ticker == ticker)
            data = session.execute(stmt)
        except Exception as exception:
            print(f"Getting {ticker} from the database failed. {exception} ")
            session.rollback()
        result = {}
        for obj in data.scalars():
            result[obj.ticker] = {'name': obj.name, 'exchange': obj.exchange,
                                  'start': obj.start, 'updated': obj.updated, 'currency': obj.currency}
    return result


@company.route('/company/suggestions/<str>', methods=['GET'])
def getSuggestions(str):
    with Session() as session:
        result = session.query(Company).filter(
            Company.name.ilike(f"%{str}%")).limit(10)
        data = []
        for row in result:
            data.append({"ticker": row.ticker, "name": row.name})

    return data
