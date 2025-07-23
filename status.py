
def checkStatus(a, b, flag):
    # code here
    if a>=1 and b>=1:
        return False
    if (a >= 1 or b >= 1) and  flag == False:
        return True
    elif (a <= -1 and b <=-1) and flag == True:
        return True
    return False    

print(checkStatus(a= 1,b= 1,flag= False))