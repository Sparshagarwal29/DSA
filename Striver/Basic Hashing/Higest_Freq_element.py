# finding the elemet which has the most occuring value in the elemet , if two value occur the same number of time retuen the smallest among them 


# brute force approch --> O(N^2) time completixity and O(1) space complexity 

class bruteforce():
    m = int(input("enter the size of array"))
    nums=[int(input("enter the value of nums"))for _ in range(m)]


    if len(nums) == 0 :
        print("-1")
        exit()

    answer = nums[0]
    maxCount = 0 

    for val in nums:
        count = 0 
        for j in range (len(nums)):
            if nums[j] == val:
                count +=1

        if (count > maxCount or (count == maxCount and val < answer)):
            maxCount = count 
            answer = val
    print("maximum frequent element ",answer )


# better approch --> "sort the array "
class betterapproch():
    m = int(input("enter the sixe of element"))
    nums = [int(input("enter the val of nums "))for _ in range(m)]
    def mostfrequentelement(self,nums):

        if len(nums) == 0:
            return -1

        nums.sort()

        answer = nums[0]
        maxCount = 0 
        start = 0 
        while start < len(nums):
            end = start
            while end < len(nums) and nums[end] == nums[start]:
                end +=1 
            count = end -start

            if (count > maxCount or (count == maxCount and nums[start] < answer)):
                maxCount = count 
                answer = nums[start]

            start = end
        return answer


# most optimal approch --> O(n) time complexity and O(1) as space complexity
# use of hashmap to store the frequency of each element 
class optimalapproch:
    m = int(input("enter the sixe of element"))
    nums = [int(input("enter the val of nums "))for _ in range(m)]
    
    def mostfrequentelemt(self,nums):

        if len(nums) == 0:
            return -1
        frequency:dict[int,int] = {}
        answer = nums[0]
        maxfrequency = 0 

        for value in nums:
            frequency[value]= frequency.get(value,0)+1  #remmber this , this is use to get the frequency of the numbes in any arr
            currentfreq = frequency[value]

            if(currentfreq > maxfrequency or (currentfreq == maxfrequency and value < answer)):
                maxfrequency = currentfreq
                answer = value
        return answer
    

        