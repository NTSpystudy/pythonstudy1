def birthdayCake(heights):
    max_ = max(heights)
    count = 0
    for height in heights:
        if height == max_:
            count +=1
    print("Colleen blowed %d candles"%count)

num = int(input("Number of Candle : ").strip())
heights = list(map(int, input("Enter each candle's height : ").strip().split(' ')))

birthdayCake(heights)
