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
    Obi : Prev_To_Play Play
    '''
    qgQuads.addQuad(["End", None, None, None])

def p_Prev_To_Play(p):
    '''
    Prev_To_Play : GoTo_Global_Vars Declare_Var GoTo_Play Prev_To_Play
    | Epsilon
    '''

# Neuralgic points

def p_GoTo_Global_Vars(p):
    '''
    GoTo_Global_Vars :
    '''
    qgQuads.fillQuad(stkSingleJumps.pop())

def p_GoTo_Play(p):
    '''
    GoTo_Play :
    '''
    stkSingleJumps.append(qgQuads.addQuad(["GoTo", None, None, None]))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Play function

# ----------------------------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Statements

# ----------------------------------------------------------------------------------------------------------------------

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
    | Declare_Var
    | Assignment
    | While_Loop
    | If_Eif_Else
    | Draw_Stmt
    '''

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Graphic Rules

# ----------------------------------------------------------------------------------------------------------------------

# Draw Statement
def p_Draw_Stmt(p):
    '''
    Draw_Stmt : DRAW Drawable SEMICOLON
    '''

# Drawables
def p_Drawable(p):
    '''
    Drawable : Circle_Func
    | Square_Func
    '''

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Drawables

# ----------------------------------------------------------------------------------------------------------------------

# Circle
# Structure: Circle(coordX, coordY, radius)
def p_Circle_Func(p):
    '''
    Circle_Func : CIRCLE PAR_OPEN Exp COMMA Exp COMMA Exp COMMA Selected_Color PAR_CLOSE
    '''
    # First we take out the radius
    intRadiusAddress = stkOperands.pop()
    strRadiusType = stkTypes.pop()

    # And validate type
    if strRadiusType == "Int" or strRadiusType == "Float":
        # We proceed
        intYAddress = stkOperands.pop()
        strYType = stkTypes.pop()

        if strYType == "Int" or strYType == "Float":
            # We proceed

            intXAddress = stkOperands.pop()
            strXType = stkTypes.pop()

            if strXType == "Int" or strXType == "Float":
                # we just take out the color
                color = p[9]

                # We make a quad
                qgQuads.addQuad(["circle", [intXAddress, intYAddress, intRadiusAddress, color], None,  None])
            else:
                generic_error("Exit with error: Type mismatch\nCircle function doesn't accept a " + strRadiusType +
                              " as a X Coord. It should be an Int or a Float")
        else:
            generic_error("Exit with error: Type mismatch\nCircle function doesn't accept a " + strRadiusType +
                          " as a Y Coord. It should be an Int or a Float")
    else:
        generic_error("Exit with error: Type mismatch\nCircle function doesn't accept a " + strRadiusType +
                      " as a radius. It should be an Int or a Float")

# ----------------------------------------------------------------------------------------------------------------------

# Square
# Structure: square(coordX, coordY, size, color)

def p_Square_Func(p):
    '''
    Square_Func : SQUARE PAR_OPEN Exp COMMA Exp COMMA Exp COMMA Selected_Color PAR_CLOSE
    '''
    # First we take out the size
    intSizeAddress = stkOperands.pop()
    strSizeType = stkTypes.pop()

    # And validate type
    if strSizeType == "Int" or strSizeType == "Float":
        # We proceed
        intYAddress = stkOperands.pop()
        strYType = stkTypes.pop()

        if strYType == "Int" or strYType == "Float":
            # We proceed

            intXAddress = stkOperands.pop()
            strXType = stkTypes.pop()

            if strXType == "Int" or strXType == "Float":
                # we just take out the color
                color = p[9]

                # We make a quad
                qgQuads.addQuad(["square", [intXAddress, intYAddress, intSizeAddress, color], None, None])
            else:
                generic_error("Exit with error: Type mismatch\nCircle function doesn't accept a " + strXType +
                              " as a X Coord. It should be an Int or a Float")
        else:
            generic_error("Exit with error: Type mismatch\nCircle function doesn't accept a " + strYType +
                          " as a Y Coord. It should be an Int or a Float")
    else:
        generic_error("Exit with error: Type mismatch\nCircle function doesn't accept a " + strSizeType +
                      " as a radius. It should be an Int or a Float")

# ----------------------------------------------------------------------------------------------------------------------
# Colors
def p_Selected_Color(p):
    '''
    Selected_Color : RED
    | GREEN
    | BLUE
    | YELLOW
    | PURPLE
    | WHITE
    | BLACK
    | ORANGE
    | CYAN
    | MAGENTA
    | PINK
    | GRAY
    '''
    p[0] = p[1]

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# I/O

# ----------------------------------------------------------------------------------------------------------------------

def p_Print(p):
    '''
    Print : PRINT PAR_OPEN Exp PAR_CLOSE SEMICOLON
    '''
    intAddress = stkOperands.pop()
    strType = stkTypes.pop()
    qgQuads.addQuad(["Print", None, None, intAddress])

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Conditionals

# ----------------------------------------------------------------------------------------------------------------------

# If_eif_else rule
def p_If_Eif_Else(p):
    '''
    If_Eif_Else : IF PAR_OPEN Exp PAR_CLOSE If_GoToF_Quad Statements_Block GoTo_Fill Eif_Recursion Optional_Else
    '''

    # Fill jumps to the end
    while len(stkMultipleJumps) > 0:
        intQuadInedx = stkMultipleJumps.pop()
        qgQuads.fillQuad(intQuadInedx)

# Eif part of the rule
def p_Eif_Recursion(p):
    '''
    Eif_Recursion : EIF PAR_OPEN Exp PAR_CLOSE If_GoToF_Quad Statements_Block GoTo_Fill Eif_Recursion
    | Epsilon
    '''

# Else part of the rule
def p_Optional_Else(p):
    '''
    Optional_Else : ELSE Statements_Block
    | Epsilon
    '''

# Neuralgic points

def p_If_GoToF_Quad(p):
    '''
    If_GoToF_Quad :
    '''
    # First, we validate the type of the resultant expression
    strType = stkTypes.pop()

    if strType != "Bool":
        generic_error("Exit with error: Type mismatch\n Expected Bool type at while.", p)
    else:
        # It's a valid expression

        # We take out the operand
        intAddress = stkOperands.pop()

        # We proceed to make the incomplete quad
        intCreatedQuadIndex = qgQuads.addQuad(["GoToF", intAddress, None, None])

        stkSingleJumps.append(intCreatedQuadIndex)

def p_GoTo_Fill(p):
    '''
    GoTo_Fill :
    '''
    # First we create a GoTo Quad for jumping to the end
    intJumpQuadIndex = qgQuads.addQuad(["GoTo", None, None, None])

    # And we add it to the stack of collective jumps
    stkMultipleJumps.append(intJumpQuadIndex)

    # Then, we fill our previous GoToF
    intPreviousJump = stkSingleJumps.pop()

    # And we fill it
    qgQuads.fillQuad(intPreviousJump)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Loops

# ----------------------------------------------------------------------------------------------------------------------

# While-loop rule
def p_While_Loop(p):
    '''
    While_Loop : WHILE Push_While_Jump PAR_OPEN Exp PAR_CLOSE While_Quad Statements_Block Fill_While_Quads
    '''

# Neuralgic Points
def p_Push_While_Jump(p):
    '''
    Push_While_Jump :
    '''
    stkSingleJumps.append(qgQuads.intNextQuad())

def p_While_Quad(p):
    '''
    While_Quad :
    '''
    # First, we validate the type of the resultant expression
    strType = stkTypes.pop()

    if strType != "Bool":
        generic_error("Exit with error: Type mismatch\n Expected Bool type at while.", p)
    else:
        #It's a valid expression

        # We take out the operand
        intAddress = stkOperands.pop()

        # We proceed to make the incomplete quad
        intCreatedQuadIndex = qgQuads.addQuad(["GoToF", intAddress, None, None])

        stkSingleJumps.append(intCreatedQuadIndex)

def p_Fill_While_Quads(p):
    '''
    Fill_While_Quads :
    '''
    intEndQuadIndex = stkSingleJumps.pop()
    intReturnQuadIndex = stkSingleJumps.pop()

    qgQuads.addQuad(["GoTo", None, None, intReturnQuadIndex])
    qgQuads.fillQuad(intEndQuadIndex)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Declarations and Assignments

# ----------------------------------------------------------------------------------------------------------------------

# Declare a variable rule

def p_Declare_Var(p):
    '''
    Declare_Var : Type ID SEMICOLON
    | Type ID ASSIGN Push_Assign Exp SEMICOLON
    '''
    # New vars type
    strNewVarType = p[1]
    strNewVarName = p[2]

    global strCurrentFunc

    if strCurrentFunc == "global":
        intAddress = gmbGlobal.intNextGlobalAddress(strNewVarType)
    else:
        intAddress = lmbLocal.intNextLocalAddress(strNewVarType)
    ftFuncsTable.addVar(strCurrentFunc, strNewVarName, strNewVarType, intAddress)

    # Optional initialization

    if len(stkOperators) > 0 and stkOperators[-1] == "=":

        # We get our result from the stack
        intResultAddress = stkOperands.pop()
        strResultType = stkTypes.pop()

        # We take out our operator
        strOperator = stkOperators.pop()

        # We validate types
        if strNewVarType == strResultType:
            # We proceed with the quad
            qgQuads.addQuad([strOperator, intResultAddress, None, intAddress])
        else:
            generic_error("Exit with error: Type mismatch.\nTrying to assign a " + strResultType + " to a " +
                          strNewVarType, p)



# Type auxiliary rule for declare var

def p_Type(p):
    '''
    Type : INT
    | FLOAT
    | BOOL
    | STRING
    '''
    p[0] = p[1]

# Neuralgic points

# ----------------------------------------------------------------------------------------------------------------------

# Assignment
def p_Assignment(p):
    '''
    Assignment : ID ASSIGN Push_Assign Exp SEMICOLON
    '''
    global strCurrentFunc

    strVarName = p[1]

    if ftFuncsTable.boolExistsVar(strCurrentFunc, strVarName):
        # We can proceed if it exists

        # First we get our vars info
        dictVarsInfo = ftFuncsTable.dictGetVarsInfo(strCurrentFunc, strVarName)
        intVarAddress = dictVarsInfo["address"]
        strVarType = dictVarsInfo["type"]

        # Then we get our result from the stack
        intResultAddress = stkOperands.pop()
        strResultType = stkTypes.pop()

        # We take out our operator
        strOperator = stkOperators.pop()

        # We validate types
        if strVarType == strResultType:
            # We proceed with the quad
            qgQuads.addQuad([strOperator, intResultAddress, None, intVarAddress])
        else:
            generic_error("Exit with error: Type mismatch.\nTrying to assign a " + strResultType + " to a " +
                            strVarType, p)

    else:
        generic_error("Exit with error: Semantic Error.\nVariable '" + strVarName + "' is not defined", p)

# Neuralgic points
def p_Push_assign(p):
    '''
    Push_Assign :
    '''
    stkOperators.append("=")


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Exp (General Expression for all statements)
def p_Exp(p):
    '''
    Exp : Logical_Or
    | Logical_Or EQUAL Push_Equal Logical_Or Equity_Quad
    | Logical_Or DIFF Push_Diff Logical_Or Equity_Quad
    '''

# Neuralgic Points

def p_Equity_Quad(p):
    '''
    Equity_Quad :
    '''
    if len(stkOperators) > 0:
        strOperator = stkOperators[-1]
        # If there are pending operations of multiplication, division or mod
        if strOperator == "==" or strOperator == "!=":
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
                         " " + strRightType + "\nAt line " + str(p.lexer.lineno))


def p_Push_Equal(p):
    '''
    Push_Equal :
    '''
    stkOperators.append("==")

def p_Push_Diff(p):
    '''
    Push_Diff :
    '''
    stkOperators.append("!=")

# ----------------------------------------------------------------------------------------------------------------------

# Logical Or rule

def p_Logical_Or(p):
    '''
    Logical_Or : Logical_And Or_Quad Multiple_Ands
    '''

# Multiple Or axiliary rule for chaining Or's

def p_Multiple_Ands(p):
    '''
    Multiple_Ands : OR Push_Or Logical_And Or_Quad Multiple_Ands
    | Epsilon
    '''

# Neuralgic Points

def p_Or_Quad(p):
    '''
    Or_Quad :
    '''
    if len(stkOperators) > 0:
        strOperator = stkOperators[-1]
        # If there are pending operations of multiplication, division or mod
        if strOperator == "or":
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
                         " " + strRightType + "\nAt line " + str(p.lexer.lineno))

def p_Push_Or(p):
    '''
    Push_Or :
    '''
    stkOperators.append("or")

# ----------------------------------------------------------------------------------------------------------------------

# Logical And rule

def p_Logical_And(p):
    '''
    Logical_And : Logical_Not And_Quad Multiple_Nots
    '''

# Multiple And auxiliary rule for chaining And's

def p_Multiple_Nots(p):
    '''
    Multiple_Nots : AND Push_And Logical_Not And_Quad Multiple_Nots
    | Epsilon
    '''

# Neuralgic Points

def p_And_Quad(p):
    '''
    And_Quad :
    '''
    if len(stkOperators) > 0:
        strOperator = stkOperators[-1]
        # If there are pending operations of multiplication, division or mod
        if strOperator == "and":
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
                         " " + strRightType + "\nAt line " + str(p.lexer.lineno))


def p_Push_And(p):
    '''
    Push_And :
    '''
    stkOperators.append("and")

# ----------------------------------------------------------------------------------------------------------------------

# Logical Not rule

def p_Logical_Not(p):
    '''
    Logical_Not : Relational
    | NOT Push_Not Relational Not_Quad
    '''

# Neuralgic points

def p_Not_Quad(p):
    '''
    Not_Quad :
    '''
    if len(stkOperators) > 0:
        strOperator = stkOperators[-1]
        # If there are pending operations of multiplication, division or mod
        if strOperator == "not":
            # We start generating the quad

            # First, we take out the right operand
            intRightOperandAddress = stkOperands.pop()
            strRightType = stkTypes.pop()

            # There is no left opperand
            intLeftOperandAddress = None
            strLeftType = None

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
                sys.exit("Exit with error: Type mismatch.\nNot valid operation: " + str(strLeftType) + " " + strOperator +
                         " " + strRightType + "\nAt line " + str(p.lexer.lineno))

def p_Push_Not(p):
    '''
    Push_Not :
    '''
    stkOperators.append("not")

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
                         " " + strRightType + "\nAt line " + str(p.lexer.lineno))


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
                         " " + strRightType + "\nAt line " + str(p.lexer.lineno))


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
                         " " + strRightType + "\nAt line " + str(p.lexer.lineno))



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
    Factor : PAR_OPEN Push_False_Bottom Exp PAR_CLOSE Pop_False_Bottom
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
    | ID Get_Id_Value
    '''

# Neuralgic Points

def p_Save_Int_Const(p):
    '''
    Save_Int_Const :
    '''
    if ftFuncsTable.table["global"]["constTable"].boolExistsConstant(p[-1], "Int"):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetConstInfo(p[-1], "Int")["address"]

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
    if ftFuncsTable.table["global"]["constTable"].boolExistsConstant(-p[-1], "Int"):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetConstInfo(-p[-1], "Int")["address"]

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
    if ftFuncsTable.table["global"]["constTable"].boolExistsConstant(p[-1], "Float"):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetConstInfo(p[-1], "Float")["address"]

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
    if ftFuncsTable.table["global"]["constTable"].boolExistsConstant(-p[-1], "Float"):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetConstInfo(-p[-1], "Float")["address"]

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
    if ftFuncsTable.table["global"]["constTable"].boolExistsConstant(p[-1], "Bool"):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetConstInfo(p[-1], "Bool")["address"]

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
    if ftFuncsTable.table["global"]["constTable"].boolExistsConstant(p[-1], "String"):
        # This constant already has an address
        intAddress = ftFuncsTable.table["global"]["constTable"].dictGetConstInfo(p[-1], "String")["address"]

    else:
        # We save constant at Global Memory
        intAddress = gmbGlobal.intNextConstantGlobalAddress("String")
        gmbGlobal.setValue(intAddress, p[-1])

        # Then we save that constant at the Funcs Directory
        ftFuncsTable.addConstant(p[-1], "String", intAddress)

    stkOperands.append(intAddress)
    stkTypes.append("String")

def p_Get_Id_Value(p):
    '''
    Get_Id_Value :
    '''
    # First, we need to validate that this var exists
    global strCurrentFunc

    strVarName = p[-1]

    if ftFuncsTable.boolExistsVar(strCurrentFunc, strVarName):
        # We get the value's info
        dictVarsInfo = ftFuncsTable.dictGetVarsInfo(strCurrentFunc, strVarName)
        intAddress = dictVarsInfo["address"]
        strType = dictVarsInfo["type"]

        # And we push them to the stacks
        stkOperands.append(intAddress)
        stkTypes.append(strType)

    else:
        generic_error("Exit with error: Variable '" + strVarName + "' not in scope", p)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Represents an empty rule
def p_Epsilon(p):
    '''
    Epsilon :
    '''
    pass

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


# Errors

def p_error(p):
    sys.exit("Syntax Error near " + str(p.value) + " at line " + str(p.lineno))

def generic_error(strMessage, p):
    sys.exit(strMessage + "\nError near line " + str(p.lexer.lineno))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


# Prints execution

def executeTest(boolDebugFunc, boolDebugQuads):
    if boolDebugFunc:
        print("-------------------------------------------")
        print("Functions Table")
        ftFuncsTable.printTable()
    if boolDebugQuads:
        print("-------------------------------------------")
        print("Quads Generated")
        qgQuads.printQuads()

    print("-------------------------------------------")
    print("Obi Machine Result:")
    obiMachine = ObiMachine(qgQuads.getQuads(), gmbGlobal, ftFuncsTable)
    obiMachine.execute(False)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# MAIN PROGRAM

# We build the parser
parser = yacc.yacc()

with open('../Tests/draw.obi', 'r') as fileObiFile:
    obiCode = fileObiFile.read()

parser.parse(obiCode, tracking=True)

# We execute the test
executeTest(False, True)