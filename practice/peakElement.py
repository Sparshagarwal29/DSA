def peakElement(arr):
        # Code here
        n = len(arr)
        if n == 1:
            return 0
        if  arr[0] > arr[1]:
            return 0
        for i in range(1,n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1] :
                return i
        if  arr[n-1] > arr[n-2]:
            return n-1
        return -1 

            

print(peakElement(arr = [-3 ,-5])) 