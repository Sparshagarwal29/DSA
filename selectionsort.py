# selection sorting 
def sort(num):
    n= len(num)
    for i in range(n):
        mini_index = i 
        for j in range(i+1,n):
            if num[j] > num[mini_index]:
                mini_index = j
        num[i],num[mini_index] = num[mini_index] , num[i]  
    return num                


num= [4,3,5,2,8,9,1,6,7]    

print(sort(num))
# t(n) ==  is O(N^2)  precise is n(n+1) /2
# space compelity is o(1)