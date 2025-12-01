from .solution import Solution

class DayOne(Solution):
    def __init__(self, solution_filepath):
        super().__init__(solution_filepath)
        self.current_position = 50

    def parse_contents(self, contents):
        pairs = []
        for line in contents:
            character = line[0]
            number = line[1:]
            pairs.append(tuple([character, int(number)]))
        return pairs

    def calculate_pair(self, pair: tuple):
        if pair[0] == "L":
            self.current_position -= pair[1]
        elif pair[0] == "R":
            self.current_position += pair[1]
        self.current_position = self.current_position % 100


    def start_solution(self):
        counter = 0
        contents = self.get_contents()
        parsed_contents = self.parse_contents(contents)
        for pair in parsed_contents:
            self.calculate_pair(pair)
            if self.current_position == 0:
                counter += 1
        print(counter)
