# [0,1,1,2,3,5,8.....]
# fibo without recusion
def fibo(n,a,b):
    if n == 0 :
        return 0
    if n==1 or n== 2:
        return 1
    for i in range(0,n):
        a , b = a+b ,  a
    return a

n=6
a =0 
b =1
print(fibo(n,a,b))


# fibo with recusion 
def fibo_rec(n):
    if n == 0 :
        return 0
    if n==1 or n== 2:
        return 1
    return fibo(n-1) + fibo(n-2)