import json
from sqlalchemy import select
import pandas as pd
from flask import Blueprint, jsonify
from markupsafe import escape

from src.controller import api_controller
from src.database.connection import session
from src.model.tables import StocksDaily

ticker = Blueprint('ticker', __name__)

@ticker.route('/ticker/<symbol>', methods=['GET', 'POST'])
def getTicker(symbol):
    data = session.query(StocksDaily).all()
    data = [ x.__dict__ for x in data ]
    data = jsonify(data)
    return data
    