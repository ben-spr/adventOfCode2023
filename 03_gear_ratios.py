from collections import deque
import pathlib
import re

import base_functions

REL_PATH_INPUT_FILE = '03_input.txt'
INPUT_PATH = pathlib.Path(__file__).parent.resolve() / REL_PATH_INPUT_FILE

SEEN = set()

NUMBERS = set('0123456789')

INPUT_STRING = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

class GearRatioSolution(base_functions.Solution):
    def solve(self):
        self.lines = base_functions.read_text_file_lines_to_list(self.input_path)
        self.lines = list(map(str.strip, self.lines))
        
        # self.lines = INPUT_STRING.split('\n')
        self.numbers = []
        self.task_1()

    def is_in_bounds(self, coordinates: tuple[int, int]):
        y, x = coordinates
        y_in_bounds = 0 <= y < len(self.lines)
        x_in_bounds = 0 <= x < len(self.lines[0])
        return y_in_bounds and x_in_bounds
    
    def task_1(self):
        height = len(self.lines)
        width = len(self.lines[0])
        seen_start_indices = set()
        seen_number_indices = set()
        start = 0
        end = 0
        for i in range(height):
            for j in range(width):
                if start < j < end:
                    continue
                current_char = self.lines[i][j]
                if (i, j) in seen_start_indices or current_char not in NUMBERS:
                    start = 0
                    end = 0
                    continue
                if not self.has_symbol_in_adjacency((i, j)):
                    continue
                seen_start_indices.add((i, j))
                start = j
                while j < width and self.lines[i][j] in NUMBERS:
                    j += 1
                end = j
                num_str = self.lines[i][start:j]
                self.numbers.append(int(num_str))
        print(sum(self.numbers))
                    

    def has_symbol_in_adjacency(self, coordinates: tuple[int, int]) -> bool:
        adjacency_matrix = [-1, 0, 1]
        stack = [coordinates]
        seen = set()
        while stack:
            i, j = stack.pop()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            try:
                current_char = self.lines[i][j]
            except IndexError:
                print(f'Index i={i}, j={j} out of range. Height: {len(self.lines)}, width: {len(self.lines[0])}.')
                continue
            if not current_char.isdigit() and current_char != '.':
                return True
            if current_char.isdigit() and i == coordinates[0]:
                # add neighbours
                for delta_y in adjacency_matrix:
                    for delta_x in adjacency_matrix:
                        if delta_y == delta_x == 0:
                            continue
                        y = i + delta_y
                        x = j + delta_x
                        if not self.is_in_bounds((y, x)) or (y, x) in seen:
                                continue
                        stack.append((y, x))
                continue
        
        return False


if __name__ == "__main__":
    solution = GearRatioSolution(INPUT_PATH)
    solution.solve()
