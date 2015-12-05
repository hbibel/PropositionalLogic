# -*- coding: utf-8 -*-

from Formulas import *

# this would be a lot nicer if I used the visitor pattern, but since this is just a homework assignment I don't 
# try to write the most beautiful code
def evaluate(fm, v):
    if type(fm) is FBoolean:
        return fm.value
    elif type(fm) is FAtom:
        return v(fm.representative)
    elif type(fm) is FNot:
        return not evaluate(fm.operand, v)
    elif type(fm) is FAnd:
        return (evaluate(fm.leftoperand, v)) and (evaluate(fm.rightoperand, v))
    elif type(fm) is FOr:
        return (evaluate(fm.leftoperand, v)) or (evaluate(fm.rightoperand, v))
    elif type(fm) is FImp:
        return (not evaluate(fm.leftoperand, v)) or evaluate(fm.rightoperand, v)
    elif type(fm) is FIff:
        return (evaluate(fm.leftoperand, v)) is (evaluate(fm.rightoperand, v))
    else: raise TypeError('This method does not support the type of object you provided.')

def atoms(fm):
    if type(fm) is FBoolean:
        return set()
    elif type(fm) is FAtom:
        return set([fm])
    elif type(fm) is FNot:
        return atoms(fm.operand)
    else:
        return atoms(fm.leftoperand).union(atoms(fm.rightoperand))

