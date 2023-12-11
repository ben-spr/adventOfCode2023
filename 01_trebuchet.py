import pathlib
import re

REL_PATH_INPUT_FILE = '01_input.txt'

def read_input_file() -> str:
    filepath = pathlib.Path(__file__).parent.resolve() / REL_PATH_INPUT_FILE
    with open(filepath, 'r') as f:
        file_text = f.read()
    return file_text

def find_numbers_in_string(text: str):
    regex = re.compile(r"\d")
    match_obj = re.findall(regex, text)
    return list(match_obj)

def find_number_from_both_sides_of_string(text: str):
    options = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    re_options = list(options.keys()) + [r'\d']
    re_option_str = '|'.join(re_options)
    
    regexes = [
        re.compile(f'(?P<number>{re_option_str})(.*)'),
        re.compile(f'(.*)(?P<number>{re_option_str})(\\D*)$')
    ]

    number = ""
    for regex in regexes:
        match = re.search(regex, text)
        digit = match.group('number')
        if options.get(digit):
            digit = digit.replace(digit, str(options.get(digit)))
        number += digit

    return int(number)


def split_text_into_lines(text: str):
    lines = text.split()
    return [line.strip() for line in lines]

def main():
    text = read_text_file_to_string()
    lines = split_text_into_lines(text)
    result = sum(list(map(find_number_from_both_sides_of_string, lines)))
    print(f"Sum of all numbers: {result}")
        


if __name__ == "__main__":
    main()
