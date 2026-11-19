# The Euclidean Algorithm is:
# Example: n1 = 20, n2 = 15

# gcd(20, 15) = gcd(20 - 15, 15) = gcd(5, 15)
# gcd(5, 15) = gcd(15 - 5, 5) = gcd(10, 5)
# gcd(10, 5) = gcd(10 - 5, 5) = gcd(5, 5)
# gcd(5, 5) = gcd(5 - 5, 5) = gcd(0, 5)
# Hence, return 5 as the GCD.


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

while a > 0 and b > 0 :
    if a > b :
        a = a % b 
    else: 
        b = b % a 
if a == 0:
    print(b) 
else: 
    print(a)