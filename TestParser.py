# -*- coding: utf-8 -*-

from Parser import defaultparser as parse
from Formulas import *

# just doing some simple checks, no need for unit tests and all that. 

# b <=> (a <=> ~a)
f1 = FIff(FAtom('b'), FIff(FAtom('a'), FNot(FAtom('a'))))
f2 = parse('b <=> (a <=> ~a)')
print str(f1 == f2)

f3 = FBoolean(True)
f4 = FBoolean(True)
f5 = FBoolean(False)
print str(f3 == f4)
print str(not f3 == f5)

# b /\ a \/ blah ==> (~a <=> ~b)
f6 = FImp(FOr(FAnd(FAtom('b'), FAtom('a')), FAtom('blah')), FIff(FNot(FAtom('a')), FNot(FAtom('b'))))
f7 = parse('b /\ a \/ blah ==> (~a <=> ~b)')
print str(f6 == f7)