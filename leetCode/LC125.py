def isPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
print(isPalindrome(s="A man, a plan, a canal: Panama"))

# isalnum -- check wheather all the character are alphanumeric, that menas they are either A-Z or a-z or 0-9 return true if they else false 