# this is the optimal soln ---> t(n) ==O(N) , s = o(1)

def maxprofit(nums):
    n = len(nums)
    max_profit = 0
    min_price = float("inf")
    for i in range(0,n):
        min_price = min(min_price,nums[i])
        max_profit = max(max_profit,nums[i]-min_price)
    return max_profit

# nums = [7,1,5,3,6,4]
nums = [3,3]
# nums = [1,2]
print(maxprofit(nums))