from collections import deque
import pathlib
import re

import base_functions

REL_PATH_INPUT_FILE = '02_input.txt'
INPUT_PATH = pathlib.Path(__file__).parent.resolve() / REL_PATH_INPUT_FILE

SEEN = set()

NUMBERS = set([number for number in "0123456789"])



class GearRatioSolution(base_functions.Solution):
    def solve(self):
        self.games = base_functions.read_text_file_lines_to_list(INPUT_PATH)
        # self.task_1()
    
    def task_1(self):
        height = len(self.games)
        width = len(self.games[0])
        for i in range(height):
            for j in range(width):
                current_char = self.games[i][j]
                if current_char in SEEN or current_char not in NUMBERS:
                    continue
                if not self.has_symbol_in_adjacency(self.games, (i, j)):
                    continue
                start = j
                while j < width and self.games[i][j] in NUMBERS:
                    j += 1
                num_str = self.games[i][start:j]
                num = int(num_str)
                    

    def has_symbol_in_adjacency(self, coordinates: tuple[int, int]) -> bool:
        i, j = coordinates
        stack = self.games[i][j]
        while stack:
            current_char = stack.pop()
            if not current_char.isalnum() and current_char != '.':
                return True
            if current_char.isdigit():
                # add neighbours
                continue


if __name__ == "__main__":
    solution = GearRatioSolution(INPUT_PATH)
    solution.solve()
