#!/usr/bin/env python3

import sys
import csv

# Identify the different items in the header
header = ["FL_DATE","OP_UNIQUE_CARRIER","OP_CARRIER_FL_NUM","ORIGIN_AIRPORT_ID","ORIGIN","ORIGIN_CITY_NAME","ORIGIN_STATE_NM","DEST_AIRPORT_ID","DEST","DEST_CITY_NAME","DEST_STATE_NM","DEP_DELAY_NEW","ARR_DELAY_NEW","CANCELLED","CANCELLATION_CODE","CARRIER_DELAY","WEATHER_DELAY","NAS_DELAY","SECURITY_DELAY","LATE_AIRCRAFT_DELAY"]
headerTranslate = dict()
for i in range(len(header)):
    headerTranslate[header[i]] = i

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # Split the line into words
    words = list(csv.reader([line]))[0]

    carrier = words[headerTranslate["OP_UNIQUE_CARRIER"]]
    
    origin = words[headerTranslate["ORIGIN"]]
    destination = words[headerTranslate["DEST"]]
    arrivalDelay = words[headerTranslate["ARR_DELAY_NEW"]]

    # Don't print if there is no data for the arrival time delay
    if arrivalDelay:
        print(f'{carrier},{origin},{destination},{arrivalDelay}')