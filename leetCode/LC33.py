def search(nums,target):
    n = len(nums)
    low = 0 
    high = n -1
    while low <= high :
        mid = (low+high) // 2
        if nums[mid] == target:
            return mid 
        if nums[mid]<=nums[high]: # this can suggest me that right side is sorted
            if target >nums[mid] and target <= nums[high]:#  nums[mid]< target <= nums[high] 
                low = mid +1
            else:
                high = mid -1
        else:
            if target < nums[mid]  and target >= nums[low]: # nums[low] =< target < nums[mid]
                high = mid -1
            else:
                low = mid +1            
    return -1


print(search(nums=[1,4,5,6,8,9,10,11,15,20],target=9))
print(search(nums=[11,15,20,1,4,5,6,8,9,10],target=9))
print(search(nums=[4,5,6,7,0,1,2],target=0))

    
