"""manages the symbol table"""

class SymbolTable:
    def __init__(self):
        self.table = {
            "R0"    : 0,
            "R1"    : 1,
            "R2"    : 2,
            "R3"    : 3,
            "R4"    : 4,
            "R5"    : 5,
            "R6"    : 6,
            "R7"    : 7,
            "R8"    : 8,
            "R9"    : 9,
            "R10"   : 10,
            "R11"   : 11,
            "R12"   : 12,
            "R13"   : 13,
            "R14"   : 14,
            "R15"   : 15,
            "SCREEN": 16384,
            "KBD"   : 24576, 
            "SP"    : 0,
            "LCL"   : 1, 
            "ARG"   : 2,
            "THIS"  : 3,
            "THAT"  : 4
        }
        self.current_free_register = 16
    
    def add_symbol(self, symbol, address): self.table[symbol] = address
    
    def get_address(self, symbol): return self.table[symbol]
    
    def next_free_register(self): self.current_free_register += 1
    
    def __contains__(self, symbol): return True if symbol in self.table.keys() else False
    