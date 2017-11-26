import ply.lex as lex
import re
import codecs
import os
import sys


reserved_words = {
    "Int" : "INT",
    "Float" : "FLOAT",
    "Int" : "INT",
    "String" : "STRING",
    "Bool" : "BOOL",
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
    "gray" : "GRAY"
}

tokens = list(reserved_words.values())


# Ignored characters
t_ignore = " \t"

print(tokens)
