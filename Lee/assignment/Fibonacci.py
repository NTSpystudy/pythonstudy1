
def Fibonacci(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return Fibonacci(n-2)+Fibonacci(n-1)

if __name__ == "__main__":
    for i in range(1,11):
        print(Fibonacci(i))