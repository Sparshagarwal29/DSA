def brute(nums,target):
    first= -1
    last = -1
    for i in range(0,len(nums)):
        if nums[i]== target:
            if first == -1:
                first = i 
            last = i
    return[first,last]

# print(brute(nums = [5,7,7,8,8,10],target=8))


def findFirst(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    result = -1
    while low <=high:
        mid = (low+high)//2
        if nums[mid] == target:
            result =  mid
            high = mid -1 
        elif nums[mid] >target:
            high = mid -1
        else:
            low = mid +1
    return result
def findLast(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    result = -1
    while low <=high:
        mid = (low+high)//2
        if nums[mid] == target:
            result =  mid
            low = mid +1
        elif nums[mid] >target:
            high = mid -1
        else:
            low = mid +1
    return result

def number(nums,target):
    first = findFirst(nums,target)
    if first == -1:
        return [-1,-1]
    else:
        second = findLast(nums,target)
        return [first,second]


        
