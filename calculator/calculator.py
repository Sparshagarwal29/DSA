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
        return "Error: Division by zero is not allowed"
    else:
        return n / m    

    
def handle_choice(choice,n,m):
        if choice == 1:
            print(addition(n,m))
        elif choice == 2:
            print(sub(n,m))
        elif choice == 3:
            print(multiplication(n,m))
        elif choice == 4:
            print(division(n,m))
        return "opreation done"
   
def main():
    while True:
        try:
            n = int(input("Enter value of n: "))
            m = int(input("Enter value of m: "))
        except ValueError:
            print("Please enter valid integers!")
            continue
        
        print("Choose operation:")
        print("1 for addition")
        print("2 for subtraction") 
        print("3 for multiplication")
        print("4 for division")
        print("5 for quitting")
        
        questions = [
            inquirer.List(
                "size",
                message="What operation do you need?",
                choices=["1", "2", "3", "4", "5"],
            ),
        ]
        
        try:
            answers = inquirer.prompt(questions)
            if answers is None:  # User cancelled
                break
            choice = int(answers['size'])
        except (ValueError, KeyboardInterrupt):
            print("Operation cancelled or invalid input")
            break
        
        if choice == 5:
            print("Goodbye!")
            break
        elif 1 <= choice <= 4:  # Fixed: Proper range check
            result = handle_choice(choice, n, m)
            print(f"Result: {result}")
        else:
            print("Invalid operation")

if __name__ == "__main__":
    main()
   