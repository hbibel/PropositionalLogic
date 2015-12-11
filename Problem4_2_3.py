# -*- coding: utf-8 -*-

from Parser import defaultparser as parse
from Util import *

bsays = parse('b <=> (a <=> ~a)')
csays = parse('c <=> ~b')
kb = FAnd(bsays, csays)
print entails(kb, FAtom('a'))
print entails(kb, FAtom('b'))
print entails(kb, FAtom('c'))