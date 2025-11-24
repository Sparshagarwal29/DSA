# we have to print the length of consective sequence it can be arranged in any format in the 


# brute force soln ---> t(n) = o(N^2) ---> TEL error 
def longConsecutive(nums):
        n = len(nums)
        max_count = 0
        for i in range(0,n):
            count = 1
            num = nums[i]
            while num+1 in nums:
                  count +=1
                  num +=1
            max_count = max(max_count,count)
        return max_count



# nums=[0,3,7,2,5,8,4,6,0,1]
# nums = [100,4,200,1,3,2]
# print(longConsecutive(nums))

# better soln 
def long(nums):
    last_smaller = float("-inf")
    count = 0 
    largest = 0
    n = len(nums)
    nums.sort()
    for i in range(0,n):
        num = nums[i]
        if num-1 == last_smaller:
                count +=1
                last_smaller = num
        elif num != last_smaller:
                count = 1 
                last_smaller = num
        largest = max(largest,count)       
    return largest
        
# nums=[0,3,7,2,5,8,4,6,0,1]   
# [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]   
# nums = [100,4,200,1,3,2]   
# print(long(nums))


# optimal soln ---> 
def longestConsecutive(nums):
    my_Set = set()
    n = len(nums)
    largest = 0

    for i in nums:
        my_Set.add(i)
    for i in my_Set:
        if i-1  not in my_Set:
            x = i
            count =1
            while x+1 in my_Set:
                count +=1
                x+=1
            largest = max(largest,count)
    return largest

nums=[0,3,7,2,5,8,4,6,0,1]   
# nums = [100,4,200,1,3,2]   
print(longestConsecutive(nums))