#!/usr/bin/env python

import sqlite3
import sys
import ConfigParser

def log_values(sensor_id, temp, hum):
    conn=sqlite3.connect('lab_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO temperatures values(datetime(CURRENT_TIMESTAMP, 'localtime'),(?), (?))""", (sensor_id,temp))
    curs.execute("""INSERT INTO humidities values(datetime(CURRENT_TIMESTAMP, 'localtime'),(?), (?))""", (sensor_id,hum))
    conn.commit()
    conn.close()

config = ConfigParser.RawConfigParser()
config.read('config.properties')
sensor = config.getboolean('DebugSection','sensor.value')
equipamento = config.get('EquipSection','equip.name')

if sensor:
    import Adafruit_DHT
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
else:
    import random
    humidity = random.randint(1,100)
    temperature = random.randint(10,30)

#grava os valores em um banco local sqlite
log_values(equipamento, temperature, humidity)
