#!/usr/local/bin/python

import sys
import os
import datetime
dateval=str(datetime.datetime.now())

clip=str(sys.argv[1])
clhw=str(sys.argv[2])
if len(sys.argv) == 4:
    hostname=str(sys.argv[3])
else:
    hostname="Not Presented"

os.chdir("/etc/sh_cmd/ip_usage_stat")

logfile = open("/var/log/dhcpd/"+clip+".log","a")
logfile.write("Commit IP: "+clip+", with MAC: "+clhw+", and NAME: "+hostname+" DATE: "+dateval+"\n")
logfile.close()
