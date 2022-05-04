from ..src.models.db_connection import connection, cursor

def test_connection():
    try:
        connection.cursor()
        connection.close()
    except:
        assert False, "Error while closing connection, or the connection was not made "