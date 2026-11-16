# lcm lowest common multiple
# Example 1:
# Input: n1 = 4, n2 = 6
# Output: 12
# Explanation: 4 * 3 = 12, 6 * 2 = 12.
# 12 is the lowest integer that is divisible both 4 and 6.



n1 = int(input("entert the first number "))
n2 = int(input("entert the second number "))

c = n1 * n2 
# lcm using eucliden algorithm 
while n1> 0 and n2>0:
    if n1 > n2 :
        n1 = n1 % n2 
    else :
        n2 = n2 % n1 
if n1 == 0 :
    print(c//n2)
else:
     print(c//n1)