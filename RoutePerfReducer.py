#!/usr/bin/env python3

import sys

# Found from OnTimePerf
worstCarriers = ["B6","G4","MQ"]

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from OnTimePerfMapper.py
    carrier, origin, destination, arrivalDelay = line.split(',')

    # Find only the bad flights we want 
    if carrier in worstCarriers:
        print(f'{carrier} {origin} {destination} {arrivalDelay}')
    
    
    