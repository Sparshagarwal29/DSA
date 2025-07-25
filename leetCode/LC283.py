# brute force soln on how to moke zero to the left side wityhout changing the order of the zon zero element 
# t(n) == o(N) and s(n)  is also o(N)
def moveZero(nums):
    temp =[]
    n = len(nums)
    for i in range(n):
        if nums[i]!= 0:
            temp.append(nums[i])
    nz = len(temp)        
    for i in range(0,len(temp)):    
        nums[i] = temp[i]   
    for i in range(nz,n):
        nums[i] = 0  
    return nums
nums=[1,0,2,4,3,0,0,3,5,1]
print(moveZero(nums))


# optimal soln -->
# method 1
def zeroShift(nums):
    i =0
    if len(nums)== 1:
        return
    while i < len(nums):
        if nums[i] == 0:
            break
        i +=1
    if i == len(nums):
            return
    j = i+1
    while j < len(nums):
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i +=1
        j +=1
    return nums
print(zeroShift(nums=[1, 0]))

