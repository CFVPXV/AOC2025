import os

def get_solutions():
    return os.listdir('solutions')

def parse_filename(name: str):
    spaced = name.replace("_", " ")
    capitalized = spaced.capitalize()
    remove_file_ext = capitalized.replace(".py", "")
    return remove_file_ext

def main():
    print("Welcome to the AOC 2025.5 solution explorer")

    if len(get_solutions()) == 0:
        print("Check back later for more solution sets")
    else:
        print("Select a solution below to view")
        for file in get_solutions():
            print(parse_filename(file))

main()
