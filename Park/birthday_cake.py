import sys

def birthdayCakeCandles(n, ar):
    candle,top_candle,top_candle_number = 0,0,0
    for candle in ar:
        if top_candle < candle:
            top_candle = candle
            top_candle_number = 0
        elif top_candle == candle:
            top_candle_number += 1
        else:
            continue

    return top_candle_number + 1

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)