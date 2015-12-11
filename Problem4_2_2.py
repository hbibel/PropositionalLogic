# -*- coding: utf-8 -*-

from Util import *
from Parser import defaultparser as parse

def printline(s):
    f = parse(s)
    print s.ljust(40) + ' | ' + str(tautology(f)).ljust(10) + ' | ' + str(satisfiable(f)).ljust(11) + ' | ' \
        + str(unsatisfiable(f)).ljust(15)

smoke = FAtom('Smoke')
fire = FAtom('Fire')
print 'Formula'.ljust(40) + ' | ' + 'tautology'.ljust(10) + ' | ' + 'satisfiable'.ljust(11) \
    + ' | ' + 'unsatisfiable'
print ''.ljust(84, '-')
s1 = 'Smoke ==> Smoke'
printline(s1)
s2 = '(Smoke ==> Fire) ==> (~Smoke ==> ~Fire)'
printline(s2)
s3 = 'Smoke \/ (Fire \/ ~Fire)'
printline(s3)
s4 = '(Fire ==> Smoke) /\ (Fire /\ ~Smoke)'
printline(s4)