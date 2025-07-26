# finially two sum hahahaha
#  [3,4,5,6]---- target is 7 so we need to find two number whoes sum would be 7 , assumeing their are only one pair as such


# brute force soln :----
# def twoSum(num : list, target : int):
#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             if num[i] + num[j] == target:
#                 return [i,j]
#     return []            

# using hash map 
# def TwoSum(num : list, target : int):
#     pass



def twoSum(nums,target):
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        print(n)
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
        


nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))    