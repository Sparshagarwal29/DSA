# find the largest element of an array 
def largest(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:  # we can also do  largest = max(largest,nums[i])
            largest = i
    return largest
# print(largest(nums=[-55,-32.-97,-99,-3,-67]))

# Find the second largest element of an rray 
#  a) brute force soln 
def sec_larg(nums):
    largest = nums[0]
    sec_large= float("-inf")
    for i in nums:
        largest = max(largest,i)
        if i > sec_large and i < largest:
            sec_large = i
    return sec_large        

print(sec_larg(nums=[55,32,97,-55,45,32,88,21]))