#    Patteern 1
#     * * * *
#     * * * *
#     * * * *
#     * * * *

def pattern1(rows, cols):
    for i in range(0,rows):
        for j in range(0,cols):
            print("*", end =" ")
        print(  )
        
# TC ==> O(N^2) 

pattern1(4,4)




# Patttern 2


#    *
#    **
#    ***
#    ****
#    *****

def pattern3(row):
    for i in range(0,row):
        for j in range(0,i):
            print("*", end =" ")
        print( )

pattern3(6)


# Pattern 3

#  1
#  1 2
#  1 2 3
#  1 2 3 4 
#  1 2 3 4 5 

def pattern3(row):
    for i in range(0,row):
        for j in range(0,i):
            print(j+1 , end =" ")
        print( )

pattern3(6)


# pattern 4 



#  1
#  2 2
#  3 3 3
#  4 4 4 4 
#  5 5 5 5 

def pattern4(row):
    for i in range(0,row):
        for j in range(0,i):
            print(i , end =" ")
        print( )

pattern4(6)



# patten 5 

#    * * * * *
# 
# 
# 
# 