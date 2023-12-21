from collections import deque
import pathlib
import re

import base_functions

REL_PATH_INPUT_FILE = '02_input.txt'
INPUT_PATH = pathlib.Path(__file__).parent.resolve() / REL_PATH_INPUT_FILE

SEEN = set()

NUMBERS = set([number for number in "0123456789"])

def task_1(games: list):
    height = len(games)
    width = len(games[0])
    for i in range(height):
        for j in range(width):
            current_char = games[i][j]
            if current_char in SEEN or current_char not in NUMBERS:
                continue
            if not has_symbol_in_adjacency(games, (i, j)):
                continue
            start = j
            while j < width and games[i][j] in NUMBERS:
                j += 1
            num_str = games[i][start:j]
            num = int(num_str)
                

def has_symbol_in_adjacency(games: list[str], coordinates: tuple(int, int)) -> bool:
    i, j = coordinates
    stack = games[i][j]
    while stack:
        current_char = stack.pop()
        if not current_char.isalnum() and current_char != '.':
            return True
        if current_char.isdigit():
            # add neighbours
            continue

def main():
    games = base_functions.read_input_file_lines_to_list(INPUT_PATH)
    task_1(games)
    # task_2(games)
    

if __name__ == "__main__":
    main()
