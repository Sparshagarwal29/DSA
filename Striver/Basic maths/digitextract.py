# count the number of digits in a number --> Tn = O(log 10 n)  and Sc = O(1)
def method1(n):
    c = 0 
    while n > 0:
        c +=1 
        n = n // 10
    return c

n = int(input("Enter a number: "))
c = method1(n)
print("The number of digits in the number is: ", c)

#  better way using log 
import math 

def method2(m):
    if m == 0:
        return 1
    import math
    return int(math.log10(m)) + 1


m = int(input("Enter a number: "))
d = method2(m)
print("The number of digits in the number is: ", d)

