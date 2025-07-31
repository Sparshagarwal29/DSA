# without recusion
def BinarySearch(nums,target):
    n = len(nums)
    low = 0 
    high = n -1
    while low <= high:
        mid = (low+ high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return - 1


# with the help of recusion 
def Search(nums,low,high,target):
    mid = (low+ high) // 2
    if low >= high:
        return -1
    if nums[mid] == target:
        return mid
    elif nums[mid]> target:
        return Search(nums,mid+1,high,target)
    else:
        return Search(nums,low,mid-1,target)
    

        
