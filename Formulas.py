# -*- coding: utf-8 -*-

class Formula(object):
    def __ne__(self, other):
        return not self.__eq__(other)

class FBoolean(Formula):
    def __init__(self, v):
        self.val = v
    def __eq__(self, other):
        return self.val == other.val

class FAtom(Formula):
    def __init__(self, r):
        self.representative = r
    def __eq__(self, other):
        return self.representative == other.representative
    def __hash__(self):
        return self.representative.__hash__()

class FNot(Formula):
    def __init__(self, o):
        self.operand = o
    def __eq__(self, other):
        return self.operand == other.operand

class FAnd(Formula):
    def __init__(self, l, r):
        self.leftoperand = l
        self.rightoperand = r
    def __eq__(self, other):
        return (self.leftoperand == other.leftoperand 
            and self.rightoperand == other.rightoperand)

class FOr(Formula):
    def __init__(self, l, r):
        self.leftoperand = l
        self.rightoperand = r
    def __eq__(self, other):
        return (self.leftoperand == other.leftoperand 
            and self.rightoperand == other.rightoperand)

class FImp(Formula):
    def __init__(self, l, r):
        self.leftoperand = l
        self.rightoperand = r
    def __eq__(self, other):
        return (self.leftoperand == other.leftoperand 
            and self.rightoperand == other.rightoperand)

class FIff(Formula):
    def __init__(self, l, r):
        self.leftoperand = l
        self.rightoperand = r
    def __eq__(self, other):
        return (self.leftoperand == other.leftoperand 
            and self.rightoperand == other.rightoperand)