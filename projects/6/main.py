from codetranslate import Code
from parser import Parser, COMMANDS
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        outfile = sys.argv[1].split(".asm", 1)[0] + ".hack"
        parser = Parser(sys.argv[1])
        code = Code()
        with open(outfile, "w") as f:
            while not parser.eof():
                d = parser.dest()
                c = parser.comp()
                j = parser.jump()
                l = parser.label()
                line = ''
                if parser.command_type() == COMMANDS.A_COMMAND: line += bin(int(l))[2:].zfill(16)
                elif parser.command_type() == COMMANDS.C_COMMAND: line += "111" + code.comp(c) + code.dest(d) + code.jump(j)
                parser.advance()
                f.write(line + "\n" if not parser.eof() else line)
        f.close()