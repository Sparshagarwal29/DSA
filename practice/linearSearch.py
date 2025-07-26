def search(nums,target):
    for i in range(0,len(nums)):
        if nums[i] == target:
            return i
    return -1
        
print(search(nums=[5,3,9,8,4,10,5,6,2],target=2))