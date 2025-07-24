def isPalindrome(x: int) :

    number_str = str(x)

    reversed_number_str = number_str[::-1]
    return number_str == reversed_number_str

print(isPalindrome(x=-121))