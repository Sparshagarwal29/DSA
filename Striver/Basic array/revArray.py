# reverse the given array 

# this is not optimal , time complexity is O(N)
n = int(input("enter the size elements "))
arr =[ int(input("enter the array elements ")) for _ in range(n)]
revarr = []
for i in range(1,n+1):
    revarr.append(arr[n-i])
print(revarr)

#  optimal soln in place two pointer O(n) and O(1){space}
left = 0 
right = n-1
while left < right:
    arr[left] , arr[right] = arr[right],arr[left]
    left +=1
    right +=1
print(arr)