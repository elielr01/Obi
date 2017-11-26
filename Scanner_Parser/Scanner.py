import ply.lex as lex
import re
import codecs
import os
import sys


reserved_words = {
    "Int" : "INT",
    "Float" : "FLOAT",
    "String" : "STRING",
    "Bool" : "BOOL",

    "true" : "BOOL_CONST",
    "false" : "BOOL_CONST",

    "play" : "PLAY",
    "if" : "IF",
    "eif" : "EIF",
    "else" : "ELSE",
    "while" : "WHILE",
    "print" : "PRINT",
    "input" : "INPUT",
    "func" : "FUNC",
    "draw" : "DRAW",
    "point" : "POINT",
    "line" : "LINE",
    "triangle" : "TRIANGLE",
    "square" : "SQUARE",
    "rectangle" : "RECTANGLE",
    "circle" : "CIRCLE",
    "polygon" : "POLYGON",
    "black" : "BLACK",
    "red" : "RED",
    "green" : "GREEN",
    "blue" : "BLUE",
    "yellow" : "YELLOW",
    "magenta" : "MAGENTA",
    "cyan" : "CYAN",
    "white" : "WHITE",
    "orange" : "ORANGE",
    "purple" : "PURPLE",
    "pink" : "PINK",
    "gray" : "GRAY",
    "and" : "AND",
    "or" : "OR",
    "not" : "NOT"
}

tokens = list(set(list(reserved_words.values()))) + [
    "INT_CONST",
    "FLOAT_CONST",
    "STRING_CONST",

    "COMMENT",
    "BLOCK_COMMENT",

    "ASSIGN",
    "PLUS_SIGN",
    "MINUS_SIGN",
    "TIMES_SIGN",
    "DIVIDE_SIGN",
    "LESS",
    "LESS_EQUAL",
    "GREATER",
    "GREATER_EQUAL",
    "EQUAL",
    "DIFF",
    "PAR_OPEN",
    "PAR_CLOSE",
    "CURLYB_OPEN",
    "CURLYB_CLOSE",
    "SQRB_OPEN",
    "SQRB_CLOSE",
    "COMMA",
    "SEMICOLON",
    "ID"
]


# Ignored characters
t_ignore = " \t"

t_ASSIGN = r"="
t_PLUS_SIGN = r"\+"
t_MINUS_SIGN = r"\-"
t_TIMES_SIGN = r"\*"
t_DIVIDE_SIGN = r"/"
t_LESS = r"<"
t_LESS_EQUAL = r"<="
t_GREATER = r">"
t_GREATER_EQUAL = r">="
t_EQUAL = r"=="
t_DIFF = r"!="
t_PAR_OPEN = r"\("
t_PAR_CLOSE = r"\)"
t_CURLYB_OPEN = r"\{"
t_CURLYB_CLOSE = r"\}"
t_SQRB_OPEN = r"\["
t_SQRB_CLOSE = r"\]"
t_COMMA = r"\,"
t_SEMICOLON = r";"

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved_words.get(t.value, 'ID')
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_BLOCK_COMMENT(t):
    r"\#\-(.|\n)*\-\#"
    pass

def t_COMMENT(t):
	r"\#.*"
	pass

def t_INT_CONST(t):
	r"\d+"
	t.value = int(t.value)
	return t

def t_FLOAT_CONST(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t

def t_STRING_CONST(t):
    r"\".*\""
    t.value = str(t.value)
    return t

def t_error(t):
    print("Lexic Error. Illegal char: '%s' at line: '%s'" % (t.value[0], t.lineno))
    t.lexer.skip(1)


scanner = lex.lex()

# print(tokens)

while True:
    tok = scanner.token()
    if not tok:
        break
    #print(tok)
