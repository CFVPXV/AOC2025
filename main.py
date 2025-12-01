import os
from solutions import day_one

def get_solutions():
    return os.listdir('solutions')

def parse_filename(name: str):
    spaced = name.replace("_", " ")
    capitalized = spaced.capitalize()
    remove_file_ext = capitalized.replace(".py", "")
    return remove_file_ext

def solution_select(choice):
    match choice:
        case "1":
            one = day_one.DayOne("inputs/DayOne/DayOne.txt")
            one.start_solution()

def main():
    print("Welcome to the AOC 2025.5 solution explorer")
    if len(get_solutions()) == 0:
        print("Check back later for more solution sets")
    else:
        print("Select a solution below to view")
        choice_num = 1
        for file in get_solutions():
            if(file != "solution.py"):
                print(f"{choice_num}: {parse_filename(file)}")
        user_choice = input("Input: ")
        solution_select(user_choice)
main()
