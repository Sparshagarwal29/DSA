# we are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a strin


# basically we need to check the last digit of the number if its odd we can say that the entire digit is odd if not we remove that last digit ans now we can check that thing again 

class soln:
    def largestOddNumber(self,num):
        if len(num) == 0:
            return ""
        for i in range(len(num),-1,-1): #{for loop range is like(start,stop,move)}
            if int(num[i])%2 != 0:
                return num[:i+1]
        return ""
            
