# we have to return the mininum elemet in the array which is rotated in any form 


def findMin(self, nums):
    target = float("inf")
    n = len(nums)
    low = 0
    high = n-1
    while low <=high:
        mid = (low+high) //2
        if nums[mid] <= nums[high]:
            target = min(target,nums[mid])
            high = mid -1
        else:
            target = min(target,nums[low])
            low = mid +1
    return target