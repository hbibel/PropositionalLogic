# -*- coding: utf-8 -*-

from Util import *

t = FBoolean(True)
f = FBoolean(False)
a = FAtom('A')
b = FAtom('B')
print ' Task                         | Result '
print '----------------------------------------'
print '4.1.1: False |= True          | ' + str(entails(f, t))
print '4.1.2: True |= False          | ' + str(entails(t, f))
print '4.1.3: (A /\\ B) |= (A <=> B)  | ' + str(entails(FAnd(a, b), FIff(a, b)))
print '4.1.4: (A <=> B) |= A \\/ B    | ' + str(entails(FIff(a, b), FOr(a, b)))
print '4.1.5: (A <=> B) |= ~A \\/ B   | ' + str(entails(FIff(a, b), FOr(FNot(a), b)))