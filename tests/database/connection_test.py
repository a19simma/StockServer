from src.database.connection import connection


def test_connection():
    try:
        connection.cursor()
        assert True
    except:
        assert False, "Error while closing connection, or the connection was not made "
