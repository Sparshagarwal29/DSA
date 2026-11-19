n = int(input("enter the number"))
dubli = n 
count = len(str(n))
sum =  0 
while n > 0 : 
    dig = n % 10 
    sum += dig ** count 
    n = n // 10 

if (sum == dubli):
    print("Armstrong number")
else:
    print("Not Armstrong number")


