# arr = [2,3,4,5,6,7,7,8,9,10]
# WE got K =14 we would be needing to find the max length with sum less than or equal to K


# brute force approach would be to find all the subarrays and check for the sum and then find the max length of the subarray with sum less than or equal to K
# this would be O(n^2) time complexity

max_length = 0 
arr = [2,5,1,7,10 ]
length = len(arr)
k = 14 

for i in range(length):
    carr_sum = 0 
    for j in range(i,length):
        carr_sum += arr[j]
        if carr_sum <= k:
            max_length = max(max_length, j-i+1 ) 
print (max_length)
