import json
from sqlalchemy import select
import pandas as pd
from flask import Blueprint, jsonify
from markupsafe import escape

from src.database.connection import initialize_session
from src.controller import api_controller
from src.model.tables import StocksDaily, Company

ticker = Blueprint('ticker', __name__)


@ticker.route('/ticker', methods=['GET', 'POST'])
def root():
    html = "<h1>This is the root of the ticker endpoint"
    html += "<p>Access the data of a specific ticker by its ticker eg. /ticker/MSFT"
    html += "<h2>Following is a list of companies:</h2>"
    html += "<ul>"

    with initialize_session() as session:
        companies = session.execute(select(Company)).scalars()
        for company in companies:
            html += "<li><b>" + str(company.ticker) + \
                "</b>: " + str(company.name)
    return html


@ticker.route('/ticker/<ticker>', methods=['GET', 'POST'])
def getTicker(ticker):
    ticker = ticker.upper()
    with initialize_session() as session:
        try:
            stmt = select(StocksDaily).where(StocksDaily.ticker == ticker)
            data = session.execute(stmt)
        except Exception as exception:
            print(f"Getting {ticker} from the database failed. {exception} ")
            session.rollback()
        result = {ticker: {}}
        for obj in data.scalars():
            result[obj.ticker][str(obj.date)] = {'open': obj.open, 'high': obj.high,
                                                 'low': obj.low, 'close': obj.close, 'volume': obj.volume, }
    return result
