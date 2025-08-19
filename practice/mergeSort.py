# merge sort --- divide and merge kind of thing 
def sotarr(left , right): #a function when given two "sorted array" merge them into a single sorted array 
    result =[]
    i,j = 0,0
    n = len(left)
    m = len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])    
            j+=1
    if i < n:
        while i< n:
            result.append(left[i])
            i +=1
    if j < m:
        while j< m:
            result.append(right[j])
            j +=1
    return result        

def mergsort(arr): #with the hel[p of recursion we are Aable to do this program 
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[: mid]
    right_arr= arr[mid :]
    left = mergsort(left_arr)
    right = mergsort(right_arr)
    return sotarr(left, right)

# time complexity === t(n) =O(n log N) log with base 2 

print(mergsort(arr=[3,4,2,8,6,1,9,2,0,11,5,7,1,2]))
