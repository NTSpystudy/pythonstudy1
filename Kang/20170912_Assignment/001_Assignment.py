def fib(num):
    if num <= 1:
        return 1
    else:
        return fib(num-1)+fib(num-2)

print('''Assingment#001_MinkyuKang
-Description-
Print Fibonacci Sequence''')
result = [1]
input_ = input("Please enter an integer number : ")

print("#Calculation Result#")

for i in range(1, int(input_)):
    result.append(fib(int(i)))

print(result)