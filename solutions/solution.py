class Solution:
    def __init__(self, solution_filepath):
        self.solution_filepath = solution_filepath

    def get_contents(self):
        contents = ""
        with open(self.solution_filepath, "r") as f:
            contents = f.read()
        return contents.split("\n")