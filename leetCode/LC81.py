def search(nums,target):
    n= len(nums)
    low = 0 
    high = n-1
    while low <= high :
        mid = (low+high) //2
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
        while nums[mid+1] == nums[mid] and (mid +1) <= n :
            mid = mid+1
        if nums[mid] <= nums[high]:
            if target >nums[mid] and target <= nums[high]:#  nums[mid]< target <= nums[high] 
                low = mid +1
            else:
                high = mid -1
        else:
            if target < nums[mid]  and target >= nums[low]: # nums[low] =< target < nums[mid]
                high = mid -1
            else:
                low = mid +1    

    return False

