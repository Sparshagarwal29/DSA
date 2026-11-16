# [1,2,3,4,5] output should be 15 
 
nums=[]
m = int(input("enter the size of array"))
for i in range(m):
    a = int(input("enter value of nums"))
    nums.append(a)
# better cleaner approch --> nums = [int(input("enter the values")) for _ in range(m)]
sum = 0 
for val in nums:
    sum+=val
print(sum)