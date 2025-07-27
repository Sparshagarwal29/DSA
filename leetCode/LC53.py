def maxSubarr(nums):
    n = len(nums)
    max_sub = float("-inf")
    for i in range(0,n):
        sub = 0 
        for j in range(i,n):
            sub += nums[j]
            if sub > max_sub:
                max_sub = sub
    return max_sub


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarr(nums))


def maxSubarry(nums):
    n = len(nums)
    maxi= float("-inf")
    total = 0 
    for i in range(0,n):
        total += nums[i]
        maxi = max(maxi,total)
        if total < 0:
            total = 0 
    return maxi



nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarry(nums))