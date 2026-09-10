N = int(input("Enter a number: "))
rev = 0 
dup = N 
while dup >0 :
    rev = rev * 10 + dup % 10 
    dup = dup // 10 

if(rev == N ):
    print("is plaindrom ")
else:
    print("is not plaindrom")