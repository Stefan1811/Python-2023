def fibonacci(n):
    if n==1 or n==0:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter the number:"))
for i in range (0,n):
    print(fibonacci(i))