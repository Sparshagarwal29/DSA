# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.


# time complexity of this solution is O(nlogn) and space complexity is O(1)

class optimalsoln:
    m = int(input("enter the sixe of element"))
    nums = [int(input("enter the val of nums "))for _ in range(m)]
    def MaxFrequency(self,nums,k):
        if len(nums) == 0:
            return -1 
        nums.sort()
        left = 0
        max_freq = 0
        total_sum = 0 
        for right in range(len(nums)):
            total_sum = total_sum+nums[right]
            while((nums[right]*(right-left+1))-total_sum) > k:  #this ((nums[right]*(right-left+1))-total_sum) would be calualting the opreation needed 
                total_sum -=nums[left]
                left +=1 
            max_freq = max(max_freq,right-left +1)
        return max_freq

               
                

