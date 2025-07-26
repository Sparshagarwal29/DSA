def twoSum(nums,target):
    hashmap = {}
    for i in range(0,len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[nums[i]] = i
    return -1

nums = [5,9,1,2,4,15,6,3]
target = 13
print(twoSum(nums,target))  