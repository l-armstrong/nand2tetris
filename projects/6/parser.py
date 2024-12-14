"""unpacks each instruction into its underlying fields"""
from enum import Enum
import sys

class COMMANDS(Enum):
    A_COMMAND   = 1 
    C_COMMAND   = 2
    LABEL       = 3

class Parser:
    def __init__(self, filename):
        self.code = [elm for elm in self.read_file(filename).split('\n') if elm != '' and not elm.startswith('//')]
        self.lineno = 0

    def read_file(self, filename):
        with open(filename) as f:
            return f.read()
    
    def eof(self):
        return self.lineno > len(self.code)
    
    def advanced(self):
        self.lineno += 1
    
    def getcommand(self):
        return self.code[self.lineno]
    

    