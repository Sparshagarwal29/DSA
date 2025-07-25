# rotate a array from the left by 1 place in thr same array 
# method 1 slicing 
def rotate(nums):
    n= len(nums)
    nums[:] = nums[-1:] + nums[0:n-1]
    return nums

nums = [5,-2,15,8,3,9,10,7]
print(rotate(nums))

# method 2 --> without slicing 
def arrRotate(nums):
    n = len(nums)
    temp = nums[-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0]= temp
    return nums    

nums = [5,-2,15,8,3,9,10,7]
print(arrRotate(nums))