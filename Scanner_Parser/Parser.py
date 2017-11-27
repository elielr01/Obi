from Scanner import *
import sys
import re
import ply.yacc as yacc
from Parser_Structures.FuncsTable import FuncsTable
from Quads.QuadsGenerator import QuadsGenerator
from Virtual_Memory.GlobalMemoryBlock import GlobalMemoryBlock
from Virtual_Memory.LocalMemoryBlock import LocalMemoryBlock
from Obi_Machine.ObiMachine import ObiMachine

# ----------------------------------------------------------------------------------------------------------------------
# INITIALIZE STRUCTURES NEEDED FOR PARSING
# ----------------------------------------------------------------------------------------------------------------------

ftFuncsTable = FuncsTable()
qgQuads = QuadsGenerator()
gmbGlobal = GlobalMemoryBlock(10000)
lmbLocal = LocalMemoryBlock(gmbGlobal.intDirBase + gmbGlobal.intMAX_BLOCK_SIZE)

stkOperators = []
stkOperands = []
stkTypes = []
stkSingleJumps = []
stkMultipleJumps = []

# We create the first GoTo quad
intCreatedQuad = qgQuads.addQuad(["GoTo", None, None, None])
stkSingleJumps.append(intCreatedQuad)


# ----------------------------------------------------------------------------------------------------------------------
# Rules
# ----------------------------------------------------------------------------------------------------------------------

def p_Obi(p):
    '''
    Obi : Play
    '''
    qgQuads.addQuad(["End", None, None, None])

def p_Play(p):
    '''
    Play : PLAY Update_First_GoTo PAR_OPEN PAR_CLOSE Statements_Block
    '''

def p_Update_First_GoTo(p):
    '''
    Update_First_GoTo :
    '''
    qgQuads.fillQuad(stkSingleJumps.pop())

def p_Statements_Block(p):
    '''
    Statements_Block : CURLYB_OPEN Multiple_Statements CURLYB_CLOSE
    '''


def p_Multiple_Statements(p):
    '''
    Multiple_Statements : Statement Multiple_Statements
    | Epsilon
    '''


def p_Statement(p):
    '''
    Statement : Print
    '''

def p_Print(p):
    '''
    Print : PRINT PAR_OPEN Expression PAR_CLOSE SEMICOLON
    '''

    intAddress = stkOperands.pop()
    strType = stkTypes.pop()
    qgQuads.addQuad(["Print", None, None, intAddress])


def p_Expression(p):
    '''
    Expression : INT_CONST Save_Int_Const
    | FLOAT_CONST Save_Float_Const
    | BOOL_CONST Save_Bool_Const
    | STRING_CONST Save_String_Const
    '''


def p_Save_Int_Const(p):
    '''
    Save_Int_Const :
    '''
    intAddress = gmbGlobal.intNextConstantGlobalAddress("Int")
    gmbGlobal.setValue(intAddress, p[-1])

    stkOperands.append(intAddress)
    stkTypes.append("Int")

def p_Save_Float_Const(p):
    '''
    Save_Float_Const :
    '''
    intAddress = gmbGlobal.intNextConstantGlobalAddress("Float")
    gmbGlobal.setValue(intAddress, p[-1])

    stkOperands.append(intAddress)
    stkTypes.append("Float")

def p_Save_Bool_Const(p):
    '''
    Save_Bool_Const :
    '''
    intAddress = gmbGlobal.intNextConstantGlobalAddress("Bool")
    gmbGlobal.setValue(intAddress, p[-1])

    stkOperands.append(intAddress)
    stkTypes.append("Bool")

def p_Save_String_Const(p):
    '''
    Save_String_Const :
    '''
    intAddress = gmbGlobal.intNextConstantGlobalAddress("String")
    gmbGlobal.setValue(intAddress, p[-1])

    stkOperands.append(intAddress)
    stkTypes.append("String")

# Represents an empty rule
def p_Epsilon(p):
    '''
    Epsilon :
    '''
    pass


def p_error(p):
    sys.exit("Syntax Error near " + str(p.value) + " at line " + str(p.lineno))



# We build the parser
parser = yacc.yacc()

with open('../Prototypes/print_arithmetics.obi', 'r') as fileObiFile:
    obiCode = fileObiFile.read()

parser.parse(obiCode, tracking=True)

#qgQuads.printQuads()
#print(qgQuads.getQuads())

obiMachine = ObiMachine(qgQuads.getQuads(), gmbGlobal, ftFuncsTable)
obiMachine.execute()