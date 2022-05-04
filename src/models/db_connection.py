import psycopg2
from .db_config import CONNECTION_STRING

connection = psycopg2.connect(CONNECTION_STRING)
cursor = connection.cursor()
