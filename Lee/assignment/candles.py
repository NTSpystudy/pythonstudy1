#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    tallest = max(ar)

    blow = 0
    for candle in ar:
	    if candle == tallest:
	        blow = blow + 1

    print(blow)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)