example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

import pathlib
import re
import time

import base_functions

REL_PATH_INPUT_FILE = '02_input.txt'

COLORS = {
    'red',
    'green',
    'blue'
}

MAX_DICE_NUMBERS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def read_game_info(line: str):
    regex = re.compile(r'(Game )(?P<game_number>\d*)(.*)')
    re_match = re.search(regex, line)
    game_number = int(re_match.group('game_number'))
    draws = line.split(':')[-1].split(';')
    return (game_number, draws)


def find_max_dice_numbers(draws: list):
    seen_colors = dict(zip(COLORS, [0]*len(COLORS)))
    regex_color_info = re.compile('( *)(?P<number>\d*)( *)(?P<color>[a-zA-Z]*)')
    for draw in draws:
        color_info_list = draw.split(',')
        for color_info in color_info_list:
            color_match = re.search(regex_color_info, color_info)
            if color_match is None:
                continue
            dice_number = int(color_match.group('number'))
            color = color_match.group('color')
            if seen_colors.get(color) is not None:
                seen_colors[color] = max(seen_colors[color], dice_number)

    return seen_colors

def task_1(games: list[str]):
    result = 0
    for game in games:
        game_number, draws = read_game_info(game)
        max_seen_colors = find_max_dice_numbers(draws)
        colors_possible = all([max_seen_colors[color] <= MAX_DICE_NUMBERS[color] for color in COLORS])
        if colors_possible:
            result += game_number
    
    print(f"The sum of all games that would have been possible with the dice set {MAX_DICE_NUMBERS} is: {result}")

def task_2(games):
    result = 0
    for game in games:
        _, draws = read_game_info(game)
        min_dice_numbers = find_max_dice_numbers(draws)
        power = 1
        for dice_number in min_dice_numbers.values():
            power *= dice_number
        result += power

    print(f"The sum of all power of dice is: {result}")

def main():
    input_path = pathlib.Path(__file__).parent.resolve() / REL_PATH_INPUT_FILE
    games = base_functions.read_input_file_lines_to_list(input_path)
    # task_1(games)
    task_2(games)
    

if __name__ == "__main__":
    main()
