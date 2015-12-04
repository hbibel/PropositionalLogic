# -*- coding: utf-8 -*-

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