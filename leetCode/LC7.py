# we have to reverse the given integer but it should not go out of the singnal 32 bit integer ==>{[-231, 231 - 1]}



def reverse( x: int):
    rev = 0 
    int_min= -2**31
    int_max= (2**31)-1
    sign = -1 if x <0 else 1
    x = abs(x)
    while x>0:
        d = x %10 
        rev = rev *10 +d
        x = x //10 
    if rev > int_max or rev <int_min:
        return 0
    else:    
        return rev * sign        

print(reverse(x=1534236469))
print(reverse(x=15342))