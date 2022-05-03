from influxdb_client import InfluxDBClient
from influx_config import args

# check influx.py file for connection arguments
client = InfluxDBClient(**args)
client.create_database('pyexample')
client.get_list_database()
