from enum import Enum
import sys

class COMMANDS(Enum): 
    A = 1
    C = 2
    LABEL = 3

# read a file
def read_file(file_name: str):
    with open(file_name) as f:
        return f.read()

def tokenize(program: str):
    tokens = [elm for elm in program.split("\n") if elm != '' and not elm.startswith('//')]
    return tokens

def find_type(token):
    pass

def parse(tokens):
    for token in tokens:
        command_type = find_type(token)


tokenize(read_file("./add/Add.asm"))