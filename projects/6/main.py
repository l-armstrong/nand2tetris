from codetranslate import Code
from parser import Parser, COMMANDS
from symboltable import SymbolTable
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        outfile = sys.argv[1].split(".asm", 1)[0] + ".hack"
        parser = Parser(sys.argv[1])
        code = Code()
        symboltable = SymbolTable()
        with open(outfile, "w") as f:
            while not parser.eof():
                d = parser.dest()
                c = parser.comp()
                j = parser.jump()
                l = parser.label()
                if parser.command_type() == COMMANDS.LABEL and l not in symboltable: 
                    symboltable.add_symbol(l, parser.ip)
                    parser.advance()
                else:
                    parser.advance()
                    parser.advance_ip()

            print(symboltable.table)
            parser.restart()
            while not parser.eof():
                d = parser.dest()
                c = parser.comp()
                j = parser.jump()
                l = parser.label()
                line = ''
                print(str(parser.lineno + 1) + ":", d, c, j, l)
                if parser.command_type() == COMMANDS.LABEL: parser.advance(); continue
                elif parser.command_type() == COMMANDS.A_COMMAND: 
                    if l in symboltable: l = str(symboltable.table[l])
                    elif l not in symboltable and not l.isdigit():
                        symboltable.add_symbol(l, symboltable.current_free_register)
                        l = str(symboltable.table[l])
                        symboltable.next_free_register()
                    line += bin(int(l))[2:].zfill(16)
                elif parser.command_type() == COMMANDS.C_COMMAND: 
                    line += "111" + code.comp(c) + code.dest(d) + code.jump(j)
                parser.advance()
                f.write(line + "\n" if not parser.eof() else line)
            print(symboltable.table)
        f.close()