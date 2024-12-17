"""unpacks each instruction into its underlying fields"""
from enum import Enum

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
        return self.lineno >= len(self.code)
    
    def advance(self):
        self.lineno += 1
    
    def getcommand(self):
        return self.code[self.lineno]
    
    def command_type(self):
        if self.code[self.lineno].startswith("@"):
            return COMMANDS.A_COMMAND
        else: return COMMANDS.C_COMMAND
    
    def dest(self):
        if self.command_type() == COMMANDS.C_COMMAND and "=" in self.code[self.lineno]:
            D = self.code[self.lineno].split("=", 1)[0]
            return D
        return None

    def comp(self):
        """D=D+A"""
        """D=D+A;JTL"""
        if self.command_type() == COMMANDS.C_COMMAND and "=" in self.code[self.lineno]:
            C = self.code[self.lineno].split("=", 1)[1]
            return C
        return None 

    def jump(self): 
        if self.command_type() == COMMANDS.C_COMMAND and ";" in self.code[self.lineno]:
            J = self.code[self.lineno].split(";", 1)[-1]
            return J
        return None
    
    def label(self):
        if self.command_type() == COMMANDS.A_COMMAND:
            A = self.code[self.lineno].split("@")[-1]
            return A
        return None
    