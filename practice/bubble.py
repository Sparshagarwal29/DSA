# bubble sort 
def bubble(num):
    n= len(num)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j] > num[j+1]:
                num[j],num[j+1] =num[j+1] ,num[j]
    return num


num =[2,4,8,5,9,3,6,1,7]
print(bubble(num))

# t(n) == n(n+1) / 2  which is again O(N^2)
# even the case is best then also the t(n) is O(N^2)

# optamised sorting
def bubbleoptimise(num):
    n= len(num)
    for i in range(n-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if num[j] > num[j+1]:
                num[j],num[j+1] =num[j+1] ,num[j]
                is_swap = True
        if is_swap == False:
            break
    return num

# for the best case t(n ) is now O(N)