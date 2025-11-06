# You should return the array of nums such that the array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.


def reaarange(nums):
    n = len(nums)
    new= [0]* n
    even_positon = 0
    odd_positon = 1
    for num in nums:
        if num < 0:
            new[odd_positon] = num
            odd_positon +=2
        if num > 0:
            new[even_positon] = num
            even_positon +=2
    return new


print(reaarange(nums=[-1,1]))