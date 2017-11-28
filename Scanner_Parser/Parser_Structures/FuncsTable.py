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
                "constTable" : VarsTable() # This is unique for this record
            },

            "play" : {
                "size" : 0,
                "params" : [],
                "varsTable" : VarsTable()
            }
        }

    # Adds a new empty function to the table
    def newFunc(self, strName):

        self.table[strName] = {
            "size" : 0,
            "params" : [],
            "varsTable" : VarsTable()
        }