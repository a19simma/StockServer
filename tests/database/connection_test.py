from src.database.connection import connection, initialize_timescale


def test_connection():
    try:
        connection.cursor()
        assert True
    except:
        assert False, "Error while closing connection, or the connection was not made "


def test_connection_error():
    try:
        initialize_timescale('asdasd')
        assert False
    except:
        assert True
