class optimalsoln:
    m = int(input("enter the sixe of element"))
    nums = [int(input("enter the val of nums "))for _ in range(m)]
    def secondhighest(self,nums):
        if len(nums) == 0:
            return -1
        hash_map ={}
        answer = nums[0]
        for num in nums:
            hash_map[num] = hash_map.get(num,0)

        max_freq = max(hash_map.values())

        second_hig = -1
        for count in hash_map.values():
            if count < max_freq and count > second_hig:
                second_hig = count

        if second_hig == -1:
            return -1 
        for num,count in hash_map.items():
            if count == second_hig and num < answer:
                answer = num
        return answer



# dic is like {key:value}
# hash_map.values() --> gives those value 
# hash_map.items() ---> this owuld be having a whole dic as output ([(key,value),(key,value)])
# so num control the key while count control the value 