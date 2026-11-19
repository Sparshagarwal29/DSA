#  we need to find the sum of the smallest and the most occuring elemt of an arr 
 

class sumation_hig_low():
    m = int(input("enter the sixe of element"))
    nums = [int(input("enter the val of nums "))for _ in range(m)]
    def sum_of_high_low(self,nums):
        if len(nums) ==0:
            return -1 
        hash_map = {}
        for num in nums:
            hash_map[num]= hash_map.get(num,0)+1
        max_freq = max(hash_map.values())
        min_freq = min(hash_map.values())
        sum = min_freq + max_freq
        return sum