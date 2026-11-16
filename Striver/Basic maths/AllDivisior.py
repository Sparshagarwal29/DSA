# Brute force  time complexity O(n)
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if n % i == 0 :
        print(i)

# optimal approch time complexity O(sqrt(n))

m = int(input("Enter a number: "))  # 
i = 1 


while i * i <= m: 
    if m % i == 0 :
        print(i)
        if i != m // i: 
            print(m // i )
    i +=1 
    