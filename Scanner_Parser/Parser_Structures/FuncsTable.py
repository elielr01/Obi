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
            "numTemps": 0
        }

    # Increments the number of temporals needed at a function. It doesn't save the temporals, because it's not needed
    def addTemp(self, funcName):
        if funcName in self.table:
            self.table[funcName]["numTemps"] +=1
            self.table[funcName]["size"] += 1
        else:
            sys.exit("Exit with error: Trying to sum a temporal var to a nonexistent function")


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
