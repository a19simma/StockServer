from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
import os

load_dotenv()
username = os.getenv('PSQL_USERNAME')
password = os.getenv('PSQL_PASSWORD')
host = os.getenv('PSQL_HOST')
port = os.getenv('PSQL_PORT')
dbname = os.getenv('PSQL_DBNAME')

CONNECTION_STRING = f"user={username} password={password} host={host} port={port} dbname=postgres"
CONNECTION_STRING_PSQL = f"user={username} password={password} host={host} port={port} dbname={dbname}"
CONNECTION_STRING_SQLALCHEMY = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"

connection = connect(CONNECTION_STRING)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

query_create = f'create database {dbname};'
query_timescale = 'CREATE EXTENSION IF NOT EXISTS timescaledb;'

try:
    cursor.execute(query_create)
except Exception as error:
    pass  # Database exists already

connection = connect(CONNECTION_STRING_PSQL)
cursor = connection.cursor()


def initialize_timescale(query):
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Exception as error:
        print(error)


initialize_timescale(query_timescale)


def initialize_session():
    engine = create_engine(CONNECTION_STRING_SQLALCHEMY)
    Session = sessionmaker(engine)
    return Session
