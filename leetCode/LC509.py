def fibo(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2,n+1):
        a,b = b,a+b
    return b


print(fibo(n=30))