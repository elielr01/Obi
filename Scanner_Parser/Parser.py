# -*- coding: utf-8 -*-
#
# Obi - Parser
#
# All the rules for Obi are defined in here, as well as the neuralgic points involved. Syntactic and Semantic
# analysis occurs in here.
#
# Author: Elí E. Linares
# ID: A00815654
# Date: Nov 27, 2017

from Scanner import *
import sys
import re
import ply.yacc as yacc
from Parser_Structures.FuncsTable import FuncsTable
from Parser_Structures.SemanticCube import SemanticCube
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
scSemanticCube = SemanticCube()

# Stacks needed to manage the neuralgic points
stkOperators = []
stkOperands = []
stkTypes = []
stkSingleJumps = []
stkMultipleJumps = []

# We create the first GoTo quad
intCreatedQuad = qgQuads.addQuad(["GoTo", None, None, None])
stkSingleJumps.append(intCreatedQuad)

# We initialize our pointer for the functions (to know in which context we are)
strCurrentFunc = "global"


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
    Play : PLAY Play_Init PAR_OPEN PAR_CLOSE Statements_Block
    '''

def p_Play_Init(p):
    '''
    Play_Init :
    '''
    global strCurrentFunc

    lmbLocal.reset()
    strCurrentFunc = "play"
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
    Print : PRINT PAR_OPEN Relational PAR_CLOSE SEMICOLON
    '''
    intAddress = stkOperands.pop()
    strType = stkTypes.pop()
    qgQuads.addQuad(["Print", None, None, intAddress])

# ----------------------------------------------------------------------------------------------------------------------

# Relationals rule

def p_Relational(p):
    '''
    Relational : Expression
    | Expression LESS Push_Less Expression Relational_Quad
    | Expression LESS_EQUAL Push_Less_Equal Expression Relational_Quad
    | Expression GREATER Push_Greater Expression Relational_Quad
    | Expression GREATER_EQUAL Push_Greater_Equal Expression Relational_Quad
    '''

# Neuralgic points

def p_Relational_Quad(p):
    '''
    Relational_Quad :
    '''
    if len(stkOperators) > 0:
        strOperator = stkOperators[-1]
        # If there are pending operations of multiplication, division or mod
        if strOperator == "<" or strOperator == "<=" or strOperator == ">" or strOperator == ">=":
            # We start generating the quad

            # First, we take out the right operand
            intRightOperandAddress = stkOperands.pop()
            strRightType = stkTypes.pop()

            # Then, we take out the left operand
            intLeftOperandAddress = stkOperands.pop()
            strLeftType = stkTypes.pop()

            # And we pop the operator from the stack
            strOperator = stkOperators.pop()

            # We validate that this operation is possible
            boolValidOperation = scSemanticCube.boolExists(strLeftType, strOperator, strRightType)

            if boolValidOperation:
                # It's a valid operation, so we ask for the resultant type
                strResultType = scSemanticCube.getType(strLeftType, strOperator, strRightType)

                global strCurrentFunc

                # We ask for the next available temporal address
                if strCurrentFunc == "global":
                    # We are in a global context
                    intResultAddress = gmbGlobal.intNextTemporalGlobalAddress(strResultType)
                else:
                    # We are in a local context
                    intResultAddress = lmbLocal.intNextTemporalLocalAddress(strResultType)

                # We make the quad
                qgQuads.addQuad([strOperator, intLeftOperandAddress, intRightOperandAddress, intResultAddress])

                # We add the temporal result to the stacks
                stkOperands.append(intResultAddress)
                stkTypes.append(strResultType)

                # We increment the temporals needed in our funcs table
                ftFuncsTable.addTemp(strCurrentFunc)
            else:
                # This is not a valid operation
                sys.exit("Exit with error: Type mismatch.\nNot valid operation: " + strLeftType + " " + strOperator +
                         " " + strRightType + "\nAt line " + str(p.lineno))


def p_Push_Less(p):
    '''
    Push_Less :
    '''
    stkOperators.append("<")

def p_Push_Less_Equal(p):
    '''
    Push_Less_Equal :
    '''
    stkOperators.append("<=")

def p_Push_Greater(p):
    '''
    Push_Greater :
    '''
    stkOperators.append(">")

def p_Push_Greater_Equal(p):
    '''
    Push_Greater_Equal :
    '''
    stkOperators.append(">=")

# ----------------------------------------------------------------------------------------------------------------------

# Expression rule

def p_Expression(p):
    '''
    Expression : Term Sum_Sub_Quad Multiple_Terms
    '''

# Multiple terms auxiliar rule to handle recursivity

def p_Multiple_Terms(p):
    '''
    Multiple_Terms : PLUS_SIGN Push_Plus_Sign Term Sum_Sub_Quad Multiple_Terms
    | MINUS_SIGN Push_Minus_Sign Term Sum_Sub_Quad Multiple_Terms
    | Epsilon
    '''

# Neuralgic points

def p_Sum_Sub_Quad(p):
    '''
    Sum_Sub_Quad :
    '''
    if len(stkOperators) > 0:
        strOperator = stkOperators[-1]
        # If there are pending operations of multiplication, division or mod
        if strOperator == "+" or strOperator == "-":
            # We start generating the quad

            # First, we take out the right operand
            intRightOperandAddress = stkOperands.pop()
            strRightType = stkTypes.pop()

            # Then, we take out the left operand
            intLeftOperandAddress = stkOperands.pop()
            strLeftType = stkTypes.pop()

            # And we pop the operator from the stack
            strOperator = stkOperators.pop()

            # We validate that this operation is possible
            boolValidOperation = scSemanticCube.boolExists(strLeftType, strOperator, strRightType)

            if boolValidOperation:
                # It's a valid operation, so we ask for the resultant type
                strResultType = scSemanticCube.getType(strLeftType, strOperator, strRightType)

                global strCurrentFunc

                # We ask for the next available temporal address
                if strCurrentFunc == "global":
                    # We are in a global context
                    intResultAddress = gmbGlobal.intNextTemporalGlobalAddress(strResultType)
                else:
                    # We are in a local context
                    intResultAddress = lmbLocal.intNextTemporalLocalAddress(strResultType)

                # We make the quad
                qgQuads.addQuad([strOperator, intLeftOperandAddress, intRightOperandAddress, intResultAddress])

                # We add the temporal result to the stacks
                stkOperands.append(intResultAddress)
                stkTypes.append(strResultType)

                # We increment the temporals needed in our funcs table
                ftFuncsTable.addTemp(strCurrentFunc)
            else:
                # This is not a valid operation
                sys.exit("Exit with error: Type mismatch.\nNot valid operation: " + strLeftType + " " + strOperator +
                         " " + strRightType + "\nAt line " + str(p.lineno))


def p_Push_Plus_Sign(p):
    '''
    Push_Plus_Sign :
    '''
    stkOperators.append("+")

def p_Push_Minus_Sign(p):
    '''
    Push_Minus_Sign :
    '''
    stkOperators.append("-")

# ----------------------------------------------------------------------------------------------------------------------

# Term Rule

def p_Term(p):
    '''
    Term : Factor Mult_Div_Mod_Quad Multiple_Factors
    '''

# Multiple Factors Auxiliar Rule for recursion
def p_Multiple_Factors(p):
    '''
    Multiple_Factors : TIMES_SIGN Push_Times_Sign Factor Mult_Div_Mod_Quad Multiple_Factors
    | DIVIDE_SIGN Push_Divide_Sign Factor Mult_Div_Mod_Quad Multiple_Factors
    | MOD_SIGN Push_Mod_Sign Factor Mult_Div_Mod_Quad Multiple_Factors
    | Epsilon
    '''

# Neuralgic Points

def p_Mult_Div_Mod_Quad(p):
    '''
    Mult_Div_Mod_Quad :
    '''
    if len(stkOperators) > 0:
        strOperator = stkOperators[-1]
        # If there are pending operations of multiplication, division or mod
        if strOperator == "*" or strOperator == "/" or strOperator == "%":
            # We start generating the quad

            # First, we take out the right operand
            intRightOperandAddress = stkOperands.pop()
            strRightType = stkTypes.pop()

            # Then, we take out the left operand
            intLeftOperandAddress = stkOperands.pop()
            strLeftType = stkTypes.pop()

            # And we pop the operator from the stack
            strOperator = stkOperators.pop()

            # We validate that this operation is possible
            boolValidOperation = scSemanticCube.boolExists(strLeftType, strOperator, strRightType)

            if boolValidOperation:
                # It's a valid operation, so we ask for the resultant type
                strResultType = scSemanticCube.getType(strLeftType, strOperator, strRightType)

                global strCurrentFunc

                # We ask for the next available temporal address
                if strCurrentFunc == "global":
                    # We are in a global context
                    intResultAddress = gmbGlobal.intNextTemporalGlobalAddress(strResultType)
                else:
                    # We are in a local context
                    intResultAddress = lmbLocal.intNextTemporalLocalAddress(strResultType)

                # We make the quad
                qgQuads.addQuad([strOperator, intLeftOperandAddress, intRightOperandAddress, intResultAddress])

                # We add the temporal result to the stacks
                stkOperands.append(intResultAddress)
                stkTypes.append(strResultType)

                # We increment the temporals needed in our funcs table
                ftFuncsTable.addTemp(strCurrentFunc)
            else:
                # This is not a valid operation
                sys.exit("Exit with error: Type mismatch.\nNot valid operation: " + strLeftType + " " + strOperator +
                         " " + strRightType + "\nAt line " + str(p.lineno))



def p_Push_Times_Sign(p):
    '''
    Push_Times_Sign :
    '''
    stkOperators.append("*")

def p_Push_Divide_Sign(p):
    '''
    Push_Divide_Sign :
    '''
    stkOperators.append("/")

def p_Push_Mod_Sign(p):
    '''
    Push_Mod_Sign :
    '''
    stkOperators.append("%")



# ----------------------------------------------------------------------------------------------------------------------

# Factor Rule

def p_Factor(p):
    '''
    Factor : PAR_OPEN Push_False_Bottom Expression PAR_CLOSE Pop_False_Bottom
    | Var_Cte
    '''

# Neuralgic Points

def p_Push_False_Bottom(p):
    '''
    Push_False_Bottom :
    '''
    stkOperators.append("(")

def p_Pop_False_Bottom(p):
    '''
    Pop_False_Bottom :
    '''
    stkOperators.pop()


# ----------------------------------------------------------------------------------------------------------------------

# Vars and Constants Rule

def p_Var_Cte(p):
    '''
    Var_Cte : INT_CONST Save_Int_Const
    | MINUS_SIGN INT_CONST Save_Neg_Int_Const
    | FLOAT_CONST Save_Float_Const
    | MINUS_SIGN FLOAT_CONST Save_Neg_Float_Const
    | BOOL_CONST Save_Bool_Const
    | STRING_CONST Save_String_Const
    '''

# Neuralgic Points

def p_Save_Int_Const(p):
    '''
    Save_Int_Const :
    '''
    if ftFuncsTable.table["global"]["constTable"].boolExistsVar(p[-1]):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetVarsInfo(p[-1])["address"]

    else:
        # We save constant at Global Memory
        intAddress = gmbGlobal.intNextConstantGlobalAddress("Int")
        gmbGlobal.setValue(intAddress, p[-1])

        # Then we save that constant at the Funcs Directory
        ftFuncsTable.addConstant(p[-1], "Int", intAddress)

    stkOperands.append(intAddress)
    stkTypes.append("Int")

def p_Save_Neg_Int_Const(p):
    '''
    Save_Neg_Int_Const :
    '''
    if ftFuncsTable.table["global"]["constTable"].boolExistsVar(-p[-1]):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetVarsInfo(-p[-1])["address"]

    else:
        # We save constant at Global Memory
        intAddress = gmbGlobal.intNextConstantGlobalAddress("Int")
        gmbGlobal.setValue(intAddress, -p[-1])

        # Then we save that constant at the Funcs Directory
        ftFuncsTable.addConstant(-p[-1], "Int", intAddress)

    stkOperands.append(intAddress)
    stkTypes.append("Int")

def p_Save_Float_Const(p):
    '''
    Save_Float_Const :
    '''
    if ftFuncsTable.table["global"]["constTable"].boolExistsVar(p[-1]):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetVarsInfo(p[-1])["address"]

    else:
        # We save constant at Global Memory
        intAddress = gmbGlobal.intNextConstantGlobalAddress("Float")
        gmbGlobal.setValue(intAddress, p[-1])

        # Then we save that constant at the Funcs Directory
        ftFuncsTable.addConstant(p[-1], "Float", intAddress)

    stkOperands.append(intAddress)
    stkTypes.append("Float")

def p_Save_Neg_Float_Const(p):
    '''
    Save_Neg_Float_Const :
    '''
    if ftFuncsTable.table["global"]["constTable"].boolExistsVar(-p[-1]):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetVarsInfo(-p[-1])["address"]

    else:
        # We save constant at Global Memory
        intAddress = gmbGlobal.intNextConstantGlobalAddress("Float")
        gmbGlobal.setValue(intAddress, -p[-1])

        # Then we save that constant at the Funcs Directory
        ftFuncsTable.addConstant(-p[-1], "Float", intAddress)

    stkOperands.append(intAddress)
    stkTypes.append("Float")

def p_Save_Bool_Const(p):
    '''
    Save_Bool_Const :
    '''
    if ftFuncsTable.table["global"]["constTable"].boolExistsVar(p[-1]):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetVarsInfo(p[-1])["address"]

    else:
        # We save constant at Global Memory
        intAddress = gmbGlobal.intNextConstantGlobalAddress("Bool")
        gmbGlobal.setValue(intAddress, p[-1])

        # Then we save that constant at the Funcs Directory
        ftFuncsTable.addConstant(p[-1], "Bool", intAddress)

    stkOperands.append(intAddress)
    stkTypes.append("Bool")

def p_Save_String_Const(p):
    '''
    Save_String_Const :
    '''
    if ftFuncsTable.table["global"]["constTable"].boolExistsVar(p[-1]):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetVarsInfo(p[-1])["address"]

    else:
        # We save constant at Global Memory
        intAddress = gmbGlobal.intNextConstantGlobalAddress("String")
        gmbGlobal.setValue(intAddress, p[-1])

        # Then we save that constant at the Funcs Directory
        ftFuncsTable.addConstant(p[-1], "String", intAddress)

    stkOperands.append(intAddress)
    stkTypes.append("String")

# ----------------------------------------------------------------------------------------------------------------------

# Represents an empty rule
def p_Epsilon(p):
    '''
    Epsilon :
    '''
    pass

# ----------------------------------------------------------------------------------------------------------------------

# Errors

def p_error(p):
    sys.exit("Syntax Error near " + str(p.value) + " at line " + str(p.lineno))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# MAIN PROGRAM

# We build the parser
parser = yacc.yacc()

with open('../Tests/print_relational.obi', 'r') as fileObiFile:
    obiCode = fileObiFile.read()

parser.parse(obiCode, tracking=True)

# We can print the Quads generated by the code.
#qgQuads.printQuads()

# We start the machine and execute it
obiMachine = ObiMachine(qgQuads.getQuads(), gmbGlobal, ftFuncsTable).execute()