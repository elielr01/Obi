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

    # This function should be used only for constants and only at Global Function
    def addConstant(self, constKey, strType, address):

        # In this case, the constant is our key, and we save the other attributes for this constant
        self.table[constKey] = {
            "type" : strType,
            "address" : address,
            "dimension" : None
        }

    # Returns true if the variable exists in the table
    def boolExistsVar(self, key):
        return key in self.table

    # Returns a dictionary with all variable's info
    def dictGetVarsInfo(self, key):
        if self.boolExistsVar(key):
            return self.table[key]
        else:
            sys.exit("Exit with error: Trying to access a nonexistent var at VarsTable. Key: " + str(key))