# longest common prefix 
#  we need to find the longest common prefix in the list 
#  Input: strs = ["flower","flow","flight"]
# Output: "fl"


# list = ["flower","flow","flight"]
# print(list[0])


# brute force 

# time complexity --> O(N*M log N)  Let N be the number of strings and M be the length of the longest string.

class Brutesoln :
      def longestcommonprefix(self,strs):
        if  not strs:
            return ""
        strs.sort()

        first = strs[0]
        last = strs[-1]
        length = 0 
        while length < len(first) and length < len(last) and first[length] == last[length]:
            length +=1 
        return first[:length]








#  optimal --> vertical scanning approch , take the char of the first string and check wheather they are present in every elemt of the list if yes then print and if found any missing character stop 
# time complexity is O(N*M)
class verticalsoln :
    def longestcommonprefix(self,strs):
        if not strs:
            return ""
        first = strs[0]
        for i in range(len(first)):
            for j in range(1, len(strs)):
                if i > len(strs[j]) and strs[j][i] != first[i]:
                    return first[:i]
        return first
            


