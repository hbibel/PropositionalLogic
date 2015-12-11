# -*- coding: utf-8 -*-

from Parser import defaultparser as parse
from Util import entails
from Formulas import FAtom, FAnd

bsays = parse('b <=> (a <=> ~a)')
csays = parse('c <=> ~b')
kb = FAnd(bsays, csays)
print 'kb |= a: ' + str(entails(kb, FAtom('a')))
print 'kb |= b: ' + str(entails(kb, FAtom('b')))
print 'kb |= c: ' + str(entails(kb, FAtom('c')))