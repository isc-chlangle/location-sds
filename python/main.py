import os
import jaydebeapi

import requests
import json
def coordinate_lookup(addr):
    value = requests.get("https://geocode.search.hereapi.com/v1/geocode?q="+addr+"&apiKey=doglPUHtDAop1ckCfGj-W5W8HqWQhgHzdCUsX9MTCy8")
    coords = value.json().get('items')[0].get('position')
    return (str(coords.get('lat')), str(coords.get('lng')))


jdbcConnectionString = os.environ.get('BUSYBOX_IRIS_JDBC_URL')
driver = 'com.intersystems.jdbc.IRISDriver'
irisUsername = 'SDSAdmin'
irisPassword = "SYS"
locTableName = "SC_Data.Location"

conn = jaydebeapi.connect(driver, jdbcConnectionString, [irisUsername, irisPassword])
curs = conn.cursor()

curs.execute("SELECT uid,street,city,stateProvince,country FROM " + locTableName + " WHERE coordinates = '' AND latitude = '' AND longitude = ''")
locsToFind = conn.fetchall()
for loc in locsToFind:
    addr = str(loc[1:])
    coords = coordinate_lookup(addr)
    curs.execute("UPDATE " + locTableName + " SET latitude='" + coords[0] + "', longitude='" + coords[1] "' WHERE uid = '" + loc[0] + "'")

curs.close()
conn.close()
