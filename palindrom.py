# palindrom by not using recursion ---> t(n) = o(N/2) which is O(N)
def palindrom(s):
    right= len(s)-1
    left = 0
    count =0
    for ch in s:
        if s[left] == s[right]:
            count +=1 
        else:
            break
        left +=1
        right -=1
    if(count == len(s)):
        return True
    else:
        return False
    
    
    
# plaindrom using recusion 
def recu_palin(s,left,right):
    if left>=right:
        return True
    if s[left] != s[right]:
        return False
    return recu_palin(s,left+1,right-1)
    
  
# s="NITIN"
s="djlfaalgjkf"
left=0
right= len(s)-1
print(palindrom(s))
print(recu_palin(s,left,right))