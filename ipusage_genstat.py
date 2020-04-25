#!/usr/local/bin/python

import sqlite3
import os

os.chdir("/etc/sh_cmd/ip_usage_stat")

reportfile = open("/var/log/dhcpd/dhcpd_free-ip.txt","w+")

conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

cursor.execute("select * from ipusage order by last_active DESC")
data=cursor.fetchall()

reportfile.write("IP\t\t\tLast Active\n")

for i in data:
    val1, ip, val2, last_seen, val3 = str(i).split("'")
    reportfile.write(ip+"\t-\t"+last_seen+"\n")

reportfile.close()
cursor.close()
