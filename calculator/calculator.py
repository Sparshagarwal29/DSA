# calculator version 1.0

import os
import sys
from pprint import pprint
sys.path.append(os.path.realpath("."))
import inquirer  # noqa

def addition(n,m):
    return n + m
def multiplication(n,m):
    if n == 0 or m == 0:
        return 0 
    else:
        return n * m
def sub(n,m):
    return n- m
def division(n,m):
    if m == 0:
        print("error")
    else:
        return n / m    
    return ("zero divisible")
    
def handle_choice(choice):
        if choice == 1:
            print(addition(n,m))
        if choice == 2:
            print(sub(n,m))
        if choice == 3:
            print(multiplication(n,m))
        if choice == 4:
            print(division(n,m))
        return "opreation done"
   

while True:
    n  = int(input("enter value of n: "))
    m =  int(input("enter value of m: "))
    print("enter the choice between 1 for addition ;"
        " 2 for sub ;"
        " 3 for multiplication ;" 
        " 4 for division ;"
        " 5 for quitting")
    questions = [
        inquirer.List(
            "size",
            message="What opreation do you need?",
            choices=["1", "2", "3", "4", "5"],
        ),
    ]

    answers = (inquirer.prompt(questions))
    choice = int(answers['size'])

    if choice == 5:
        break
    elif choice == 1 or 2 or 3 or 4:
        print(handle_choice(choice))
    else:
        print("invaid opreation")  