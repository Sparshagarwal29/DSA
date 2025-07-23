# program to check whaether the array is sorted or not 
def check(nums):
    n = len(nums) -1
    for i in range(0,n):
        if nums[i] > nums[i+1]:
            return False
    return True

print(check(nums=[3,5,6,8,9,10,20]))
print(check(nums=[1,2,5,3,6,8,9,11,13]))

# we have to keep the unique elment a first then the space left we can keep any element of our chice , we have to do all this in place meaning in the same inped arr 
# we have to return the number of unique number 
def dubli(nums):
    n = len(nums)
    if n ==1:
        return 1
    i = 0 
    j = i+1
    while j < n:
        if nums[j] != nums[i]:
            i +=1
            nums[i],nums[j] = nums[j] , nums[i]
        j +=1
    print(nums)        
    return i+1                    

print(dubli(nums=[1,1,1,1,1,2,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9]))
            
    