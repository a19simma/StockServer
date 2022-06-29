import json
from sqlalchemy import select
import pandas as pd
from flask import Blueprint, jsonify
from markupsafe import escape

from src.controller import api_controller
from src.database.connection import session
from src.model.tables import StocksDaily

ticker = Blueprint('ticker', __name__)


@ticker.route('/ticker/<ticker>', methods=['GET', 'POST'])
def getTicker(ticker):
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
