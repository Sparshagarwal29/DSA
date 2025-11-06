# find the number in the list with even number of digits 


def findNumbers(nums):
    n = len(nums)
    digit = 0
    for i in range(0,n):
        m = nums[i]
        count = 0
        while m > 0:
            d = m % 10
            count +=1
            m = m//10
            # print(count)
        if count % 2 == 0:
            digit +=1
    return digit 

print(findNumbers(nums=[555,901,482,1771]))


def EvenNumbers(nums):
    digit = 0
    for i in nums:
        m = i
        num_digit= len(str(m))
        if (num_digit)%2 == 0:
            digit +=1
    return digit 

print(EvenNumbers(nums=[555,901,482,1771]))