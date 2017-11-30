# -*- coding: utf-8 -*-

# Obi - VarsTable
#
# Class that represents  the Variables Directory
#
# Author: Elí E. Linares
# ID: A00815654
# Date: Nov 27, 2017

import sys

class VarsTable:

    # Constructor
    def __init__(self):

        # The vars table is represented by a dictionary of dictionaries
        #
        # Table:
        # 1. Key = varName
        # 1. Value = Dictionary with var's info (varsInfo)
        #
        # VarsInfo:
        # 1. Key = type
        # 1. Value = string with var's type
        #
        # 2. Key = address
        # 2. Value = int with var's address
        #
        # 3. Key = dimension
        # 3. Value = List of DimNodes (if it's an array) or None (if it's atomic
        self.table = {}

    # ------------------------------------------------------------------------------------------------------------------
    # ConsTable methods
    # ------------------------------------------------------------------------------------------------------------------

    # Returns true if the constant exists in the table
    def boolExistsConstant(self, key, strType):
        return (key in self.table) and (self.table[key]["type"] == strType)

    # This function should be used only for constants and only at Global Function
    def addConstant(self, constKey, strType, address):

        # In this case, the constant is our key, and we save the other attributes for this constant
        self.table[constKey] = {
            "type" : strType,
            "address" : address,
            "dimension" : None
        }

    # Returns a dictionary with all const's info
    def dictGetConstInfo(self, key, strType):
        if self.boolExistsConstant(key, strType):
            return self.table[key]
        else:
            sys.exit("Exit with error: Trying to access a nonexistent var at ConstTable. Key: " + str(key))

    # ------------------------------------------------------------------------------------------------------------------
    # VarsTable methods
    # ------------------------------------------------------------------------------------------------------------------

    # Returns true if a variable's name is already in the table
    def boolExistsVar(self, strName):
        return strName in self.table

    # Adds new var to the vars table
    def addVar(self, strName, strType, intAddress):
        # We validate if this var already exists
        if self.boolExistsVar(strName):
            # Already declared var
            sys.exit("Exit with error: Variable '" + strName + "' already declared")

        # If it doesn't exist, we can freely add it
        self.table[strName] = {
            "type" : strType,
            "address" : intAddress,
            "dimension" : None
        }

    # Returns a dictionary with all var's info
    def dictGetVarsInfo(self, strName):
        if self.boolExistsVar(strName):
            return self.table[strName]
        else:
            sys.exit("Exit with error: Trying to access a nonexistent var at VarsTable. Var name: " + strName)

    # Prints the whole funcs directory
    def printTable(self):
        for key, value in self.table.items():
            print("\t\t" + str(key) + ":")
            for key2, value2 in value.items():
                print("\t\t\t" + str(key2) + ": " + str(value2))