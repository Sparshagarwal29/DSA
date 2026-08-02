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

def pattern2(row):
    for i in range(0,row):
        for j in range(0,i):
            print("*", end =" ")
        print( )

pattern2(6)


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


print("\n\n")


# patten 5 

#    * * * * *
#    * * * * 
#    * * * 
#    * * 
#    * 

def pattern5(rows):
    for i in range(rows):
        for j in range(rows-i):
            print("*", end =" ")
        print(  )

pattern5(5)


print("\n\n")


# 1 2 3 4 5
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

def pattern6(rows):
    for i in range(rows):
        for j in range(rows-i):
            print(j+1, end =" ")
        print(  )

pattern6(5)

print("\n\n")


#       *
#      ***
#     *****
#    *******
#   *********

def pattern7(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        for j in range(rows-i-1):
            print(" ",end=" ")
        print(" ")

pattern7(5)


print("\n\n")

#   *********
#    *******
#     *****
#      ***
#       *

def pattern8(rows):
    for i in range(rows):
        for j in range(i):
            print(" ",end=" ")
        for j in range(2*(rows-i)-1):
            print("*",end=" ")    
        for j in range(i):
            print(" ",end=" ")
        print(" ")

pattern8(5)


print("\n\n")


# Pattern 9 


#       *
#      ***
#     *****
#    *******
#   *********
#   *********
#    *******
#     *****
#      ***
#       *


def pattern9(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        for j in range(rows-i-1):
            print(" ",end=" ")
        print(" ")
    for i in range(rows):
        for j in range(i):
            print(" ",end=" ")
        for j in range(2*(rows-i)-1):
            print("*",end=" ")
        for j in range(i):
            print(" ",end=" ")
        print(" ")


pattern9(5)

print("\n\n")

# pattern 10 

# *
# * * 
# * * * 
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# * 


def pattern10(rows):
    for i in range(2*rows - 1 ):
        if i < rows :
            stars = i +1 
        else:
            stars = 2 * rows - i -1
        for j in range(stars):
            print("*", end=" ")
        print()
        


pattern10(5)

# pattern 11 

# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 

def pattern11(rows):
    for i in range(rows):
        for j in range():


pattern11(5)




# pattern 12 

#  1             1
#  1 2         2 1 
#  1 2 3     3 2 1
#  1 2 3 4 4 3 2 1 


# pattern 13.

# 1 
# 2 3 
# 4 5 6
# 7 8 9 10 
# 11 12 13 14 15 


#  pattern 14


# A 
# A B
# A B C 
# A B C D
# A B C D E 


#  PATTERN 15 

# A B C D E 
# A B C D
# A B C 
# A B
# A 


# pattern 16 
# A 
# BB 
# CCC
# DDDD
# EEEEE

# pattern 17 
#     A
#    ABA
#   ABCBA
#  ABCDCBA

# pattern 18

# E
# D E
# C D E
# B C D E
# A B C D E