# -*- coding: utf-8 -*-

from Formulas import *
from itertools import combinations

# this would be a lot nicer if I used the visitor pattern, but since this is just a homework assignment I don't 
# try to write the most beautiful code
def evaluate(fm, v):
    if type(fm) is FBoolean:
        return fm.val
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

def onallvaluations(fm):
    ats = map(lambda a: a.representative, atoms(fm))    
    alltrue = True
    for i in range(len(ats) + 1):
        cs = set(combinations(ats, i)) # all subsets of ats of length i
        for tupl in cs:
            evalresult = evaluate(fm, lambda x: x in tupl)
            alltrue = evalresult and alltrue
            if not alltrue:
                return False
    return alltrue

def tautology(fm):
    return onallvaluations(fm)

def unsatisfiable(fm):
    return tautology(FNot(fm))

def satisfiable(fm):
    return not unsatisfiable(fm)

def entails(f1, f2):
    f = FAnd(f1, FNot(f2))
    return unsatisfiable(f)