def maxOne(nums):
    count= 0 
    max_count = 0
    for i in nums:
        if i == 1:
            count +=1
        else:
            max_count = max(max_count,count)
            count= 0 
    return max(max_count,count)


print(maxOne(nums=[1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0]))
        
        
        

        
