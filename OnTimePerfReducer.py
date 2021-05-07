#!/usr/bin/env python3

import sys

# carrier: (totalDelay, num flights)
delays = dict()

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from OnTimePerfMapper.py
    carrier, currentDelay = line.split(',')

    # Update the running total of delays and number of flights for a given carrier
    if carrier not in delays:
       delays[carrier] = (float(currentDelay),1)
    else:
        totalDelay, numFlights = delays[carrier]
        totalDelay += float(currentDelay)
        numFlights += 1
        delays[carrier] = (totalDelay,numFlights)

# Print out the average for each carrier 
for carrier in delays.keys():
    totalDelay, numFlights = delays[carrier]
    print(f'{carrier} {totalDelay/numFlights}')
