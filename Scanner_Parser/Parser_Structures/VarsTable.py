# -*- coding: utf-8 -*-

# Obi - VarsTable
#
# Class that represents  the Variables Directory
#
# Author: Elí E. Linares
# ID: A00815654
# Date: Nov 27, 2017

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

    #def addVar(self, strName, strType):
