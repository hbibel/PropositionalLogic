# -*- coding: utf-8 -*-

from Formulas import *

def ispunctuation(c):
    return c in '()[]{},'

def issymbolic(c):
    return c in '~´!@#$%^&*-+=|\\:;<>.?/'

def isnumeric(c):
    return c in '0123456789'

def isalphanumeric(c):
    return c in 'abcdefghijklmnopqrstuvwxyz_\'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lexwhile(prop, inp):
    if inp == "":
        return "", inp
    if prop(inp[0]):
        tok, rest = lexwhile(prop, inp[1:])
        tok = inp[0:1] + tok
    else:
        tok, rest = "", inp
    return tok, rest

def lex(inp):
    _, inp = lexwhile(str.isspace, inp)
    if inp == "":
        return []
    c = inp[0]
    cs = inp[1:]
    if isalphanumeric(c):
        prop = isalphanumeric
    elif issymbolic(c):
        prop = issymbolic
    else:
        prop = lambda x: False
    tokt1, rest = lexwhile(prop, cs)
    tokt1 = c + tokt1
    return [tokt1] + lex(rest)

# <=>
def parseexpression(inp): # inp = list of tokens
    e1, i1 = parseimp(inp)
    if len(i1) > 0 and i1[0] == '<=>':
        e2, i2 = parseexpression(i1[1:])
        return FIff(e1, e2), i2
    return e1, i1

# =>
def parseimp(inp):
    e1, i1 = parseor(inp)
    if len(i1) > 0 and  i1[0] == '==>':
        e2, i2 = parseor(i1[1:])
        return FImp(e1, e2), i2
    return e1, i1

# \/
def parseor(inp):
    e1, i1 = parseand(inp)
    if len(i1) > 0 and  i1[0] == '\\/':
        e2, i2 = parseand(i1[1:])
        return FOr(e1, e2), i2
    return e1, i1

# /\
def parseand(inp):
    e1, i1 = parsenegation(inp)
    if len(i1) > 0 and  i1[0] == '/\\':
        e2, i2 = parsenegation(i1[1:])
        return FAnd(e1, e2), i2
    return e1, i1

# ~
def parsenegation(inp):
    if inp[0][0] == '~':
        e1, i1 = parseatom(inp[1:])
        return FNot(e1), i1
    return parseatom(inp)

# atom
def parseatom(inp):
    if inp == []:
        raise ValueError("Missing token. Expected an atomic expression here. Misformed input?")
    if ispunctuation(inp[0][0]):
        e2, i2 = parseexpression(inp[1:]) # i2 here is actually i2[1:] in Harrison
        if ispunctuation(i2[0][0]): # TODO: Check for actual closing bracket
            return e2, i2[1:]
        else:
            raise ValueError("I could not found a closing bracket...")
    return FAtom(inp[0]), inp[1:]

def makeparser(parser, s):
    expr, rest = parser(lex(s))
    if rest == []:
        return expr
    else:
        raise AssertionError("Unparsed input: " + str(rest))

def defaultparser(s):
    return makeparser(parseexpression, s)