# count the number of odd number in the array 

m = int(input("enter the size of array"))
nums=[int(input("enter the value of nums"))for _ in range(m)]
count = 0 
for val in nums:
    if val % 2 !=0 :
        count+=1 
print(count)
