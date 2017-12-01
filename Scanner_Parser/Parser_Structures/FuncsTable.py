# -*- coding: utf-8 -*-

# Obi - FuncsTable
#
# Class that represents  the Functions Directory
#
# Author: Elí E. Linares
# ID: A00815654
# Date: Nov 27, 2017

from VarsTable import VarsTable
import sys

class FuncsTable:

    # Constructor
    def __init__(self):

        # Every time a program starts, Global function and Play function are initialized

        # The funcs table is represented by a dictionary of dictionaries
        #
        # Table:
        # 1. Key = funcName
        # 1. Value = Dictionary with func's info (funcsInfo)
        #
        # FuncsInfo:
        # 1. Key = size
        # 1. Value = quantity of required memory (size of function)
        #
        # 2. Key = params
        # 2. Value = List with the required types of params (if needed) in order
        #
        # 3. Key = varsTable
        # 3. Value = Instance of VarsTable class
        self.table = {
            # The global function is the only one that will have a Constants Table
            "global" : {
                "size" : 0,
                "params" : [],
                "varsTable" : VarsTable(),
                "constTable" : VarsTable(), # This is unique for this record
                "numTemps" : 0
            },

            "play" : {
                "size" : 0,
                "params" : [],
                "varsTable" : VarsTable(),
                "numTemps" : 0
            }
        }

    # ------------------------------------------------------------------------------------------------------------------
    # ConsTable methods
    # ------------------------------------------------------------------------------------------------------------------

    # Adds a new constant to the ConstTable
    def addConstant(self, constKey, strType, intAddress):
        self.table["global"]["constTable"].addConstant(constKey, strType, intAddress)
        self.table["global"]["size"] += 1

    # ------------------------------------------------------------------------------------------------------------------
    # VarsTable methods
    # ------------------------------------------------------------------------------------------------------------------

    # Validate existance of a var
    def boolExistsVar(self, strFuncName, strName):
        if strFuncName in self.table:
            return (self.table[strFuncName]["varsTable"].boolExistsVar(strName) or
                    self.table["global"]["varsTable"].boolExistsVar(strName))
        else:
            sys.exit("Exit with error: Validating existance of a new var within a nonexistent function")

    # Adds new var to a function's vars table
    def addVar(self, strFuncName, strName, strType, intAddress):
        if strFuncName in self.table:
            self.table[strFuncName]["varsTable"].addVar(strName, strType, intAddress)
            self.table[strFuncName]["size"] += 1
        else:
            sys.exit("Exit with error: Add new var to a nonexistent function")

    # Returns a dictionary with vars info
    def dictGetVarsInfo(self, strFuncName, strName):
        if strFuncName in self.table:
            if self.table[strFuncName]["varsTable"].boolExistsVar(strName):
                return self.table[strFuncName]["varsTable"].dictGetVarsInfo(strName)
            elif self.table["global"]["varsTable"].boolExistsVar(strName):
                return self.table["global"]["varsTable"].dictGetVarsInfo(strName)
            else:
                sys.exit("Exit with error: Var named '" + strName + "' is not declared.")
        else:
            sys.exit("Exit with error: Getting var's info within a nonexistent function")

    # ------------------------------------------------------------------------------------------------------------------
    # FuncsTable methods
    # ------------------------------------------------------------------------------------------------------------------

    # Adds a new empty function to the table
    def newFunc(self, strName):

        if strName in self.table:
            sys.exit("Exit with error: Syntax Error. There's a function already named '" + strName + "'")

        self.table[strName] = {
            "size": 0,
            "params": [],
            "varsTable": VarsTable(),
            "numTemps": 0,
            "quad" : 0
        }

    # Increments the number of temporals needed at a function. It doesn't save the temporals, because it's not needed
    def addTemp(self, funcName):
        if funcName in self.table:
            self.table[funcName]["numTemps"] +=1
            self.table[funcName]["size"] += 1
        else:
            sys.exit("Exit with error: Trying to sum a temporal var to a nonexistent function")

    # Adds the type of a param to the "params" column
    def addParam(self, strFuncName, strParamName, strParamType, intParamAddress ):
        if strFuncName in self.table:
            # The function exists so...

            # First we save the param type
            self.table[strFuncName]["params"].append(strParamType)

            # Then, we save the param at it's VarsTable
            self.addVar(strFuncName, strParamName, strParamType, intParamAddress)

        else:
            sys.exit("Exit with error: Trying to save a param whithin a nonexistent function")

    # Validate existance of a var
    def boolExistsParam(self, strFuncName, strParamName):
        if strFuncName in self.table:
            return self.table[strFuncName]["varsTable"].boolExistsVar(strParamName)
        else:
            sys.exit("Exit with error: Validating existance of a new param within a nonexistent function")

    # Save initial quad index of a function
    def saveInitialQuad(self, strFuncName, intInitialQuad):
        if strFuncName in self.table:
            self.table[strFuncName]["quad"] = intInitialQuad
        else:
            sys.exit("Exit with error: Saving initial quad within a nonexistent function")

    def intGetInitialQuad(self, strFuncName):
        if self.boolExistFunc(strFuncName):
            return self.table[strFuncName]["quad"]
        else:
            sys.exit("Exit with error: Getting initial quad from a nonexistent function")

    # Returns true if the function exists
    def boolExistFunc(self, strFuncName):
        return strFuncName in self.table

    def boolValidParam(self, strFuncName, strParamType ,intParamIndex):
        if self.boolExistFunc(strFuncName) and (len(self.table[strFuncName]["params"]) > intParamIndex):
            # We search for the param
            return strParamType == self.table[strFuncName]["params"][intParamIndex]
        else:
            sys.exit("Exit with error: Validating param within a nonexistent function")

    def intNumberOfParams(self, strFuncName):
        if self.boolExistFunc(strFuncName):
            return len(self.table[strFuncName]["params"])
        else:
            sys.exit("Exit with error: Trying to get number of params of a nonexistent function")

    # Prints the whole funcs directory
    def printTable(self):
        for key,value in self.table.items():
            print(str(key))
            for key2, value2 in value.items():
                if isinstance(value2, VarsTable):
                    print("\t" + str(key2) + ":")
                    value2.printTable()
                else:
                    print("\t" + str(key2) + ": " + str(value2))
