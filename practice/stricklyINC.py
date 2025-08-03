# a given array should be first strictly increasing then strictly deceasing then again structly increasing eg --[1,4,9,8,2,11,12]

def check(nums):
    i = 1
    n = len(nums)
    if nums[0] > nums[i]:
        return False
    if n < 4:
        return False
    while i < n and nums[i] > nums[i-1]:
        i +=1
    if i== 1 or i == n:
        return False
    while i < n and nums[i] < nums[i-1]:
        i +=1
    if i== 1 or i == n:
        return False
    while i < n and nums[i] > nums[i-1]:
        i +=1
    if i== 1:
        return False
    return i == n

print(check(nums=[1,3,5,4,2,6,8]))