def last(s):
    s =s.rstrip()
    count = 0
    for char in s[::-1]:
        if char != ' ':
            count +=1
        else:
            break
    return count


print(last(s="hello  world    "))