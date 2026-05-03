# arr = [2,3,4,5,6,7,7,8,9,10]
# WE got K =14 we would be needing to find the max length with sum less than or equal to K


# brute force approach would be to find all the subarrays and check for the sum and then find the max length of the subarray with sum less than or equal to K
# this would be O(n^2) time complexity
def longest_subarray(arr, k):
    max_length = 0 
    length = len(arr)

    for i in range(length):
        carr_sum = 0 
        for j in range(i,length):
            carr_sum += arr[j]
            if carr_sum <= k:
                max_length = max(max_length, j-i+1 ) 
            elif carr_sum > k:
                break
    print (max_length)


# Better soln 
# i need to form a window 
# tc - O(2N)
def longest_subarray_sliding_window(arr, k):
    l = 0 
    r = 0 
    n = len(arr)
    carr_sum = 0
    max_length = 0 

    while (r < n ):
        carr_sum += arr[r]
        while carr_sum > k:
            carr_sum -= arr[l]
            l +=1 
        if carr_sum <= k :
            max_length =  max(max_length, r-l+1 )
        r +=1 
    print(max_length)


    # best soln 
    # somehow from O(2N) to O(N)
    # so this works only when we need to fing the length of the longest subarray with sum less than or equal to K not when need to find the subarray itself
    def longest_subarray_sliding_window_optimal(arr, k):
        l = 0 
        r = 0 
        n = len(arr)
        carr_sum = 0
        max_length = 0 

        while (r < n ):
            carr_sum += arr[r]
            if carr_sum > k:
                carr_sum -= arr[l]
                l +=1 
            if carr_sum <= k :
                max_length =  max(max_length, r-l+1 )
            r +=1 
        print(max_length)

