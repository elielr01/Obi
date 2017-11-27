from VarsTable import VarsTable
import sys

class FuncsTable:

    def __init__(self):

        self.table = {
            "global" : {
                "size" : 0,
                "params" : [],
                "varsTable" : VarsTable()
            },

            "play" : {
                "size" : 0,
                "params" : [],
                "varsTable" : VarsTable()
            }
        }

    def newFunc(self, strName):

        self.table[strName] = {
            "size" : 0,
            "params" : [],
            "varsTable" : VarsTable()
        }