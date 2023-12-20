import pathlib

def read_input_file_to_string(path: pathlib.Path) -> str:
    filepath = path
    with open(filepath, 'r') as f:
        file_text = f.read()
    return file_text

def read_input_file_lines_to_list(path: pathlib.Path) -> list:
    filepath = path
    line_list = []
    with open(filepath, 'r') as f:
        for line in f:
            line_list.append(line)

    return line_list
