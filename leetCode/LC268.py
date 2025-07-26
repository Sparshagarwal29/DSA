# method 1 --> a just for python code ---> hogh t(n) == N^2
def missing(nums):
    n = len(nums)
    for i in range(0,n):
        if i not in nums:
            return i


print(missing(nums=[1,2,3,4,5,8,7,9,0]))

# meethod 2 --> genralized way -->t(n) ==o(N)
def miss(nums):
    n = len(nums)
    hashmap= {}
    for i in nums:
        hashmap[nums[i]] = True
    for i in range (0,n):
        if i not in hashmap:
            return i 
        

print(missing(nums=[1,2,5,3,6,7,3,8,9,0]))


# method 3 --> T(n) = o(N) --> little more simple {real T(n){O(3N)}}
def mis(nums):
    freq = {}
    n = len(nums)
    for i in range(0,n+1):
        freq[i] = 0
    for i in nums:
        freq[i] = 1
    for k,u in freq.items():
        if u == 0 :
            return k 
        
print(missing(nums=[1,2,5,3,6,7,3,8,9,0]))

# {
#     a very simple way is to find the sum of nums and find the 0 to len of nums then subtract both --- that number
# }


