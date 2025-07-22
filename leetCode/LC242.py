# two string need to check wheather  the element of the second string exists in first string 
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
    


print(isAnagram(s="rat",t="car"))