import json


def read_text_file_to_string(path):
    with open(path, 'r') as f:
        file_text = f.read()
    return file_text

def read_json_file(path):
    with open(path, 'r') as f:
        file_json = f.read()
    return file_json
