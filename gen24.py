from fronius_to_influx import FroniusToInflux
from influxdb import InfluxDBClient
from astral import LocationInfo

import pytz


client = InfluxDBClient(host='localhost', port=8086, username='grafana', password='grafana', ssl=False)
client.switch_database('grafana')
location = LocationInfo(('Warsaw', 'Poland', 'Europe/Warsaw', 52.4, 16.9, 90))
tz = pytz.timezone('Europe/Warsaw')
endpoints = [
    "http://192.168.30.254/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=3PInverterData&DeviceId=1",
    "http://192.168.30.254/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=CommonInverterData&DeviceId=1"
#    "http://192.168.30.254/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=CumulationInverterData&DeviceId=1"
]

z = FroniusToInflux(client, location, endpoints, tz)
z.IGNORE_SUN_DOWN = False
z.run()
