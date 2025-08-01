def num(nums,target):
    n = len(nums)
    ceil,floor = -1,-1
    low,high = 0,n-1
    while low <=high:
        mid = (low+high) // 2
        if nums[mid] == target:
            return[nums[mid],nums[mid]]
        elif nums[mid]>target:
            high = mid -1 
            ceil = nums[mid]
        else:
            floor = nums[mid]
            low = mid +1
    return [ceil,floor]      