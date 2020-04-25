#!/usr/local/bin/python

from datetime import date
import time
import sqlite3
import os
import datetime

ipfirstdigits="192.168.1."
ipfirst=1
iplast=254
iprange=[]
deleteitem=[]
working_date="1970-01-01"
dbname="database.sqlite"

os.chdir("/etc/sh_cmd/ip_usage_stat")

def initiprange():
    global iprange
    global working_date
    global deleteitem
    iprange=[]
    deleteitem=[]
    for i in range(ipfirst, iplast+1):
        iprange.append(i)
    working_date=(date.today()).strftime("%Y-%m-%d")


if not os.path.isfile(dbname):
    needinitfirst=True
else:
    needinitfirst=False

conn = sqlite3.connect(dbname)
cursor = conn.cursor()

initiprange()

if needinitfirst:
    cursor.execute("CREATE TABLE ipusage (ip text, last_active text)")
    for i in range(0, len(iprange)):
        hostip=ipfirstdigits + str(iprange[i])
        cursor.execute("INSERT into ipusage VALUES ('"+hostip+"', 'never seen before')")
    conn.commit()


while True:
    if (working_date == (date.today()).strftime("%Y-%m-%d") and iprange):
        for i in iprange:
            hostip=ipfirstdigits + str(i)
            if not os.system("ping -c 1 -t 1 -q " + hostip):
                cursor.execute("UPDATE ipusage SET last_active = '"+working_date+"' WHERE ip = '"+hostip+"'")
                deleteitem.append(i)
        conn.commit()
        if deleteitem:
            for i in deleteitem:
                iprange.remove(i)
            deleteitem=[]
            os.system('python ipusage_genstat.py')
        time.sleep(600)
    else:
        time.sleep(1800)
        initiprange()
