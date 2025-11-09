# we need to check f the nmber in a array repeats itself or nor 
#  hashing === always remmber hashing concept if repation type tings come 
def count(nums):
    hashmap={}
    for i in nums:
        if i in hashmap:
            return True
        hashmap[i]= hashmap.get(i, 0) +1
    return False



# method - 2  by using hashmap 
def count_2(nums):
    seen = set()
    for num in nums:
        if num  in seen:
            return True
        seen.add(num)
    return False


print(count(nums=[1,2,3]))    