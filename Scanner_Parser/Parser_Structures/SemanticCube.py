# -*- coding: utf-8 -*-

# Obi - SemanticCube
#
# Class that represents the semantic cube where we store the return types for each operation
#
# Author: Elí E. Linares
# ID: A00815654
# Date: Nov 27, 2017

class SemanticCube:

    # Constructor
    def __init__(self):

        # The semantic cub is represented as a dictionary
        #
        # DictSemanticCube:
        # Key = A tuple with the operands types and operators needed to identify an operation
        # Value = String with return type
        self.dictSemanticCube = {

            # ----------------------------------------------------------------------------------------------------------
            # Ints
            # ----------------------------------------------------------------------------------------------------------

            # Int vs Int
            ("Int", "+", "Int") : "Int",
            ("Int", "-", "Int"): "Int",
            ("Int", "*", "Int"): "Int",
            ("Int", "/", "Int"): "Float",
            ("Int", "%", "Int"): "Int",

            # Int vs Float
            ("Int", "+", "Float"): "Float",
            ("Int", "-", "Float"): "Float",
            ("Int", "*", "Float"): "Float",
            ("Int", "/", "Float"): "Float",
            ("Int", "%", "Float"): "Float",

            # ----------------------------------------------------------------------------------------------------------
            # Floats
            # ----------------------------------------------------------------------------------------------------------

            # Float vs Int
            ("Float", "+", "Int"): "Float",
            ("Float", "-", "Int"): "Float",
            ("Float", "*", "Int"): "Float",
            ("Float", "/", "Int"): "Float",
            ("Float", "%", "Int"): "Float",

            # Float vs Float
            ("Float", "+", "Float"): "Float",
            ("Float", "-", "Float"): "Float",
            ("Float", "*", "Float"): "Float",
            ("Float", "/", "Float"): "Float",
            ("Float", "%", "Float"): "Float"
        }

    # Returns true if the operation exists in the Semantic Cube
    def boolExists(self, strLeftType, strOperator, strRightType):
        tplKey = (strLeftType, strOperator, strRightType)
        return tplKey in self.dictSemanticCube

    # Returns the resultant type of an operation
    def getType(self, strLeftType, strOperator, strRightType):

        if self.boolExists(strLeftType, strOperator, strRightType):
            tplKey = (strLeftType, strOperator, strRightType)
            return self.dictSemanticCube[tplKey]
        else:
            return None

    # Prints the semantic cube (for debugging)
    def printSemanticCube(self):

        for key, value in self.dictSemanticCube:
            print(str(key) + " : " + str(value))
