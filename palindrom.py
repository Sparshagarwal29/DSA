# palindrom by not using recursion 
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
        print("is palindrom")  
    else:
        print("not a plaindrom")              
    return s

  
s="SPARSH"
print(palindrom(s))