def mergearr(num,arr):
    result = []
    n = len(num)
    m = len(arr)
    i =0 
    j = 0 
    while i < n  and j < m:
            if num[i] <= arr[j]:
                if num[i] not in result:
                    result.append(num[i])
                i +=1
            else:
                if arr[j] not in result:
                    result.append(arr[j])
                j +=1
              
    while i < n:
        if num[i] not in result:
            result.append(num[i])
        i +=1
    while j < m:
        if arr[j] not in result:
            result.append(arr[j])
        j +=1
    return result

print(mergearr(num=[1,1,3,5,7],arr=[2,2,5,7,8,9,10,11]))
    


            
