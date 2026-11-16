# finding the elemet which has the most occuring value in the elemet , if two value occur the same number of time retuen the smallest among them 


# brute force approch 
m = int(input("enter the size of array"))
nums=[int(input("enter the value of nums"))for _ in range(m)]
if len(nums) == 0 :
    print("-1")
