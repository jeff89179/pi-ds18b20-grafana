#!/usr/bin/python

import os
import time
from influxdb import InfluxDBClient

influx_host = '10.80.25.33'
host = 'dc-pi'
port = '18086'
dbname = 'dctemps'
user = ' '
password = ' '
#temp_sensor1 = '/sys/bus/w1/devices/28-0316a194c4ff/w1_slave'
temp_sensor3 = '/sys/bus/w1/devices/28-0516a47f87ff/w1_slave'

client = InfluxDBClient(influx_host, port, user, password, dbname)
client.create_database(dbname)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


def temp_raw():
    f = open(temp_sensor3, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def get_data_points():
    temperature = read_temp()
    iso = time.ctime()
    json_body = [
            {
                "measurement": "temp_sensor3_vessel_celcius",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": temperature,
                    }
                }

            ]

    return json_body


while True:
    json_body = get_data_points()
    client.write_points(json_body)
    print (json_body)
    time.sleep(1)
