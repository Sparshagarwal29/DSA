# method 1 with slicing 
# def rotate(nums,k):
#     n = len(nums)
#     nums[:] = nums[n-k:] + nums[:n-k]

# nums = [1,2]
# k = 7
# rotate(nums,k)
# print(nums)

# method 2 -->without slicing 
def arrRotate(nums,k):
    n = len(nums)
    def reverse(nums,left,right):
        while left< right:
            nums[left],nums[right] = nums[right],nums[left]
            left +=1
            right -=1
    reverse(nums,n-k,n-1) 
    reverse(nums,0,n-k-1)
    reverse(nums,0,n-1)       
nums = [1,2,3,4,5,6,7]
k = 3
arrRotate(nums,k)
print(nums)