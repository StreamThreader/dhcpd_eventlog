#!/usr/local/bin/python3.6

import sys
import os
import datetime
dateval=str(datetime.datetime.now())

numargs = len(sys.argv) - 1

if numargs >= 1:
    clip=str(sys.argv[1])
else:
    clip="Not Presented"

if numargs >= 3:
    hostname=str(sys.argv[3])
else:
    hostname="Not Presented"

if numargs >= 2:
    clhw=str(sys.argv[2])
else:
    clhw="Not Presented"

logfile = open("/var/log/dhcpd/"+clip+".log","a")
logfile.write("Commit IP: "+clip+", with MAC: "+clhw+", and NAME: "+hostname+" DATE: "+dateval+"\n")
logfile.close()
