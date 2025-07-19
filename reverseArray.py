# reverse an array with left and right means from a partiular index to a particular index using recusion 
def reverse(num,left,right):
    if left >= right:
        print (num)
        return
    num[left],num[right]  = num[right],num[left]
    return reverse(num,left+1,right-1)

# same program using while loop without recursion
def reverseUsingWhile(num, left, right):
    while(left >=right):
        num[left],num[right]  = num[right],num[left]
        left +=1
        right +=1
    print (num)        



num =[1,2,7,6,5,4,3,8,9,10,11,12]
left = 2
right = 6
reverse(num,left,right)
reverseUsingWhile(num, left, right)