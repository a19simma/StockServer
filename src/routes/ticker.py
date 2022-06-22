import sqlalchemy as sql
import pandas as pd
from flask import Blueprint

from src.controller import api_controller

ticker = Blueprint('ticker', __name__)

@ticker.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"