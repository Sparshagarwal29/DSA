# check the array is sorted or not {ascending order}


m = int(input(""))
nums=[int(input(""))for _ in range(m)]
for i in range(m):
    if nums[i-1] > nums[i]:
        print("False")
    else:
        print("True")

