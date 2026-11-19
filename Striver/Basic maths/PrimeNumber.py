import math 
n =int(input("enter the number"))
if n < 2:
    print("not prime")
for i in range (2, int(math.sqrt(n)+1 )) : 
    if n % i ==0: 
        print("not prime")
        break
    else:
        print("Prime")
        break