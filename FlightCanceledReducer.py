#!/usr/bin/env python3

import sys

# code : count
cancellationCounts = dict()


for line in sys.stdin:
    # Remove leading and trailing whitespace
    code = line.strip()

    if code not in cancellationCounts:
        cancellationCounts[code] = 1
    else:
        cancellationCounts[code] = cancellationCounts[code] + 1


for code in cancellationCounts.keys():
    print(f'{code} {cancellationCounts[code]}')


