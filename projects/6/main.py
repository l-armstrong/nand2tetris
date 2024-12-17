from parser import Parser
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        parser = Parser(sys.argv[1])
        while not parser.eof():
            print(parser.dest(), parser.comp(), parser.jump(), parser.label())
            parser.advance()