# -*- coding: utf-8 -*-
from Util import *
from Parser import defaultparser as parse
import sys

def main():
    while True:
        line = raw_input('\nPlease enter a formula. Press Enter to finish the input. Write \'q\' to exit the program.\n')
        if line == 'q':
            sys.exit()
        fm = parse(line)
        if satisfiable(fm):
            print line + ' is satisfiable.'
        else:
            print line + ' is not satisfiable.'
        if tautology(fm):
            print line + ' is a tautology.'
        else:
            print line + ' is not a tautology.'

if __name__ == '__main__':
    main()