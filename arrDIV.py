#  check weather the number of a list{array } divides all the number in the list 
import sys
def arr(num):
    min_values = sys.maxsize
    for i in num:
        if i < min_values:
            min_values = i
            
    for j in  num:
        if not j % min_values == 0:
            return False
    return True
                


num = [4,2,88,44,66,62,86,122,22,28,64,36,72,92]
print(arr(num))