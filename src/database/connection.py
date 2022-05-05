from dotenv import load_dotenv
from psycopg2 import connect
import os

load_dotenv()
username = os.getenv('PSQL_USERNAME')
password = os.getenv('PSQL_PASSWORD')
host = os.getenv('PSQL_HOST')
port = os.getenv('PSQL_PORT')
dbname = os.getenv('PSQL_DBNAME')

CONNECTION_STRING = f"postgres://{username}:{password}@{host}:{port}/{dbname}"
connection = connect(CONNECTION_STRING)
cursor = connection.cursor()
