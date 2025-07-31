def sort(nums):
    n = len(nums)
    countzero = 0 
    countone = 0 
    counttwo = 0 
    for i in nums:
        if i == 0:
            countzero +=1
        elif i == 1:
            countone +=1
        else:
            counttwo +=1
    for i in range(0,countzero):
        nums[i] = 0
    for i in range(countzero,countzero+countone):
        nums[i] = 1
    for i in range(countzero+countone,n):
        nums[i] = 2
    return nums

print(sort(nums=[2,0,1,0,0,1,1,0,2]))
