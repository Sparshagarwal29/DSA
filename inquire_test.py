import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer  # noqa
questions = [
    inquirer.List(
        "size",
        message="What size do you need?",
        choices=["1", "2", "3", "4", "5"],
    ),
]

answers = inquirer.prompt(questions)
# choice = int(answers.values())
# print(choice)
choice = int(answers['size'])
print(choice)
print(answers.values(), type)
 
