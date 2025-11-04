# 3sum we have to return triplet [nums[i], nums[j], nums[k]] such that such that i != j , i!=k , j != k and num[i] + nums[j] + nums[k] = 0 



# brute force soln -- t(n) = O(N^3)
def sum(nums):
    n = len(nums)
    result = set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):                
                    if (nums[i]+nums[j]+nums[k]) == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        result.add(tuple(temp))
    return [list(ans) for ans in result]


print(sum(nums=[-1,0,1,2,-1,-4]))
# better soln t(n) = O(N^2)
def sun(nums):
    n = len(nums)
    result = set()
    for i in range(0,n):
        my_set = set()
        for j in range(i+1,n):
            k  = -(nums[i]+nums[j])     
            if k in my_set:
                temp = [nums[i],nums[j],k]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])
    return [list(ans) for ans in result]

print(sun(nums=[-1,0,1,2,-1,-4]))
              
# optimal t(n) = O(N)
def threeSum(nums):
    n = len(nums)
    result = []
    nums.sort()
    for i in range(n):
        if i !=0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = n-1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -=1
            else:
                temp = [nums[i],nums[j],nums[k]]
                result.append(temp)
                j +=1
                k -=1
                while nums[j] == nums[j-1]:
                    j +=1
                while nums[k] == nums[k-1]:
                    k -=1
    return result
print(threeSum(nums=[-1,0,1,2,-1,-4]))
            
            


            
            



