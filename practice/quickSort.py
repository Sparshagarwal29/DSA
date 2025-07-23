def postion(arr,low,high):
    i = low
    j = high 
    pivot= arr[low]
    while i < j:
        while arr[i] <= pivot and i <= high-1:
            i +=1
        while arr[j] > pivot and j >= low-1:
            j -=1
        if i <j:
            arr[i],arr[j] = arr[j],arr[i]            
    arr[low],arr[j] =arr[j],arr[low]  
    return j  # we return j so that we can get the index postion of pivot as that index would help to find the new low and new high 

def qucikSort(arr,low,high):
    if low<high:
        p_index = postion(arr,low,high)
        qucikSort(arr,low,p_index-1) 
        qucikSort(arr,p_index+1,high)

arr = [2,8,6,4,3,9,11,77,55,22,4,8,1,4]
high= 13
low = 0
qucikSort(arr,low,high)
print(arr)


                    