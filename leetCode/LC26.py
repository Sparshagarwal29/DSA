def removeDuplicates(nums):
    n = len(nums)
    i = 0 
    j = i+1
    if n == 1:
        return 1 
    while j < n:
        if nums[i] != nums[j]:
            i +=1
            nums[i] = nums[j]    
        j +=1    
    return i + 1