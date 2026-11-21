# isomorphic string 


# time complexity is O(N)
#  space complexity is O(k)
class soln:
    def isIsomorphic(self,s,t):
        if len(s) != len(t):
            return False 
        hashmap = {}
        my_set = set()
        for i in range(len(s)):
            if s[i] not in hashmap :
                if t[i] in my_set:
                    return False
                hashmap[s[i]] = t[i] 
                my_set.add(t[i])
            elif hashmap[s[i]] != t[i]:
                return False
        return True
            
