def isAnagram(s,t):
    if len(s) != len(t):
        return False
    hashMap ={}
    hashMap1 ={}
    for i in range(len(s)):
        hashMap[s[i]] = hashMap.get(s[i],0) +1
        hashMap1[t[i]] = hashMap1.get(t[i],0) +1
    # print(hashMap1)
    if hashMap1 == hashMap:
        return True 

def groupAnagrams(strs):
    hashMap ={}
    for i in  range (len(strs)) :
        for j in range(i+1,len(strs)):
            if (isAnagram(strs[i],strs[j])):
                hashMap[strs[j] ]= hashMap.get(strs[j],0) +1
    return hashMap                
        



print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))