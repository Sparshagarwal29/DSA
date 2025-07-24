# [0,1,1,2,3,5,8.....]
# fibo without recusion ---> good t(n)
def fibo(n,a,b):
    if n == 0 :
        return 0
    if n==1 :
        return 1
    for i in range(2,n+1):
        a , b = b ,  a+b
    return b

n=30
a =0 
b =1
print(fibo(n,a,b))


# fibo with recusion ---> not good for t(n) == o(n^2)
def fibo_rec(n):
    if n == 0 :
        return 0
    if n==1 or n== 2:
        return 1
    return fibo_rec(n-1) + fibo_rec(n-2)