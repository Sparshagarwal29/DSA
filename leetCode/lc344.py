class solution:
    def reverse_string(self,s):
        if(len(s)) == 0 :
            return -1 
        left = 0 
        right = len(s) -1 

        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1 
            right -=1 