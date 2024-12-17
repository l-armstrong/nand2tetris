"""manages the symbol table"""

class SymbolTable:
    def __init__(self):
        self.table = {}
    
    def add_symbol(self, symbol, address):
        self.table[symbol] = address
    
    def get_address(self, symbol):
        return self.table[symbol]
    
    def __contains__(self, symbol):
        return True if symbol in self.table.keys() else False
    