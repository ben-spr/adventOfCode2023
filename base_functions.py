import abc
import json
import re
import pathlib


class Solution:
    def __init__(self, path_to_input_file: str):
        if not self.validate_input_file_path(path_to_input_file):
            raise FileNotFoundError(f'File not found: {path_to_input_file}')
        self.input_path = path_to_input_file
        # self.input_str = read_text_file_to_string(path_to_input_file)
        
    @abc.abstractmethod
    def solve(self):
        pass

    def validate_input_file_path(self, path_to_input_file: pathlib.Path):
        regex = re.compile('[\\/,\\\\](?P<filename>.*).txt$')
        return not re.search(regex, str(path_to_input_file)) is None
        

def read_text_file_to_string(path: pathlib.Path) -> str:
    with open(path, 'r') as f:
        file_text = f.read()
    return file_text

def read_text_file_lines_to_list(path: pathlib.Path) -> list:
    filepath = path
    with open(filepath, 'r') as f:
        line_list = f.readlines()

    return line_list

def read_json_file(path: pathlib.Path) -> dict:
    with open(path, 'r') as f:
        file_json = json.load(f)
    return file_json
