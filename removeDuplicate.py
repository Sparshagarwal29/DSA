# program to check whaether the array is sorted or not 
def check(nums):
    n = len(nums) -1
    for i in range(0,n):
        if nums[i] > nums[i+1]:
            return False
    return True

print(check(nums=[3,5,6,8,9,10,20]))
print(check(nums=[1,2,5,3,6,8,9,11,13]))