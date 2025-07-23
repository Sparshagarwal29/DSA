# palindrom by not using recursion ---> t(n) = o(N/2) which is O(N)
# def palindrom(s):
#     right= len(s)-1
#     left = 0
#     count =0
#     for ch in s:
#         if s[left] == s[right]:
#             count +=1 
#         else:
#             break
#         left +=1
#         right -=1
#     if(count == len(s)):
#         return True
#     else:
#         return False
    
    
    
# plaindrom using recusion 
# def recu_palin(s,left,right):
#     if left>=right:
#         return True
#     if s[left] != s[right]:
#         return False
#     return recu_palin(s,left+1,right-1)
    


def isPalindrome(s: str):
    result = s.lower().replace(" ","")
    print(result)
    left = 0 
    count = 0
    right = len(result) -1
    for ch in result:
        if result[left] == result[right]:
            count +=1
        else:
            break 
        left +=1
        right -=1
    if (count == len(result)):
        return True    
    return False         
  
# s="NITIN"
# s="djlfaalgjkf"ṇ
# left=0
# right= len(s)-1
# print(palindrom(s))
# print(recu_palin(s,left,right))
print(isPalindrome(s="Was it a car or a cat I saw?"))