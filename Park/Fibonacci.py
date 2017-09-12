fibonacci = [1,1]
i = 0
while i < 10:
    fibonacci.append(fibonacci[i] + fibonacci[i+1])
    i += 1

print(fibonacci)