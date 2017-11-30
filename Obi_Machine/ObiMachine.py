import sys
import turtle
from turtle import Turtle
from Virtual_Memory.MemoryManager import MemoryManager

class ObiMachine:

    def __init__(self, lstlstQuads, gmbGlobal, ftFuncsTable):

        self.lstlstQuads = lstlstQuads
        self.mmMemoryManager = MemoryManager(gmbGlobal)
        self.ftFuncsTable = ftFuncsTable
        self.t = Turtle()
        self.t.penup()
        self.t.ht()



    def execute(self, boolDebugMode):

        intQuadIndex = 0
        while self.lstlstQuads[intQuadIndex][0] != "End":

            # ----------------------------------------------------------------------------------------------------------
            # IO Code
            # ----------------------------------------------------------------------------------------------------------
            if self.lstlstQuads[intQuadIndex][0] == "Print":
                #execute print code
                print(self.mmMemoryManager.getValueFrom(self.lstlstQuads[intQuadIndex][3]))
                intQuadIndex += 1

            # ----------------------------------------------------------------------------------------------------------
            # Jumps Codes
            # ----------------------------------------------------------------------------------------------------------

            elif self.lstlstQuads[intQuadIndex][0] == "GoTo":
                # Execute a Jump
                intQuadIndex = self.lstlstQuads[intQuadIndex][3]

            elif self.lstlstQuads[intQuadIndex][0] == "GoToF":
                # Execute a jump on false
                # Cases:
                # 1. [ GoToF , 100  , None , 2 ]
                # 2. [ GoToF , [100] , None , 2 ]

                # First we get our result value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intResultAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intResultAddress = self.mmMemoryManager.getValueFrom(intResultAddrAddr)
                else:
                    # It's directly an address
                    intResultAddress = self.lstlstQuads[intQuadIndex][1]

                # With the result address, we ask for the result value
                resultValue = self.mmMemoryManager.getValueFrom(intResultAddress)
                #sys.exit("Debug exit: " + str(resultValue))
                #self.mmMemoryManager.printMemory()

                if not resultValue:
                    # Execute jump
                    intQuadIndex = self.lstlstQuads[intQuadIndex][3]
                else:
                    # We just continue
                    intQuadIndex += 1


            # ----------------------------------------------------------------------------------------------------------
            # Arithmetics Codes
            # ----------------------------------------------------------------------------------------------------------

            elif self.lstlstQuads[intQuadIndex][0] == "+":
                # Execute sum code
                # Cases:
                # 1. [ + , 100  , 102 , 200 ]
                # 2. [ + , [100] , 102 , 200 ]
                # 3. [ + , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the sum
                result = leftValue + rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "-":
                # Execute subtract code
                # Cases:
                # 1. [ - , 100  , 102 , 200 ]
                # 2. [ - , [100] , 102 , 200 ]
                # 3. [ - , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the subtraction
                result = leftValue - rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "*":
                # Execute multiplication code
                # Cases:
                # 1. [ * , 100  , 102 , 200 ]
                # 2. [ * , [100] , 102 , 200 ]
                # 3. [ * , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the multiplication
                result = leftValue * rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "/":
                # Execute division code
                # Cases:
                # 1. [ / , 100  , 102 , 200 ]
                # 2. [ / , [100] , 102 , 200 ]
                # 3. [ / , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the division
                result = leftValue / rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "%":
                # Execute mod code
                # Cases:
                # 1. [ % , 100  , 102 , 200 ]
                # 2. [ % , [100] , 102 , 200 ]
                # 3. [ % , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the mod
                result = leftValue % rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            # ----------------------------------------------------------------------------------------------------------
            # Relational Codes
            # ----------------------------------------------------------------------------------------------------------

            elif self.lstlstQuads[intQuadIndex][0] == "<":
                # Execute less_than code
                # Cases:
                # 1. [ < , 100  , 102 , 200 ]
                # 2. [ < , [100] , 102 , 200 ]
                # 3. [ < , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the less_than
                result = leftValue < rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "<=":
                # Execute less_equal code
                # Cases:
                # 1. [ <= , 100  , 102 , 200 ]
                # 2. [ <= , [100] , 102 , 200 ]
                # 3. [ <= , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the less_equal
                result = leftValue <= rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == ">":
                # Execute greater_than code
                # Cases:
                # 1. [ > , 100  , 102 , 200 ]
                # 2. [ > , [100] , 102 , 200 ]
                # 3. [ > , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the greater_than
                result = leftValue > rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == ">=":
                # Execute greater_equal code
                # Cases:
                # 1. [ >= , 100  , 102 , 200 ]
                # 2. [ >= , [100] , 102 , 200 ]
                # 3. [ >= , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the greater_equal
                result = leftValue >= rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            # ----------------------------------------------------------------------------------------------------------
            # Logical Codes
            # ----------------------------------------------------------------------------------------------------------

            elif self.lstlstQuads[intQuadIndex][0] == "not":
                # Execute not code
                # Cases:
                # 1. [ not , None  , 102 , 200 ]
                # 2. [ not , None , [102] , 200 ]

                # First, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the logical not
                result = not rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "and":
                # Execute and code
                # Cases:
                # 1. [ and , 100  , 102 , 200 ]
                # 2. [ and , [100] , 102 , 200 ]
                # 3. [ and , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the logical and
                result = leftValue and rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "or":
                # Execute or code
                # Cases:
                # 1. [ or , 100  , 102 , 200 ]
                # 2. [ or , [100] , 102 , 200 ]
                # 3. [ or , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the logical or
                result = leftValue or rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            # ----------------------------------------------------------------------------------------------------------
            # Equity Codes
            # ----------------------------------------------------------------------------------------------------------

            elif self.lstlstQuads[intQuadIndex][0] == "==":
                # Execute equality code
                # Cases:
                # 1. [ == , 100  , 102 , 200 ]
                # 2. [ == , [100] , 102 , 200 ]
                # 3. [ == , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the equality
                result = leftValue == rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "!=":
                # Execute diff code
                # Cases:
                # 1. [ != , 100  , 102 , 200 ]
                # 2. [ != , [100] , 102 , 200 ]
                # 3. [ != , 100 , [102] , 200 ]

                # First, we get left value
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intLeftAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intLeftAddress = self.mmMemoryManager.getValueFrom(intLeftAddrAddr)
                else:
                    # It's directly an address
                    intLeftAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                leftValue = self.mmMemoryManager.getValueFrom(intLeftAddress)


                # Then, we get the right address
                if isinstance(self.lstlstQuads[intQuadIndex][2], list):
                    # If it's a list, that's an address of an address
                    intRightAddrAddr = self.lstlstQuads[intQuadIndex][2][0]
                    intRightAddress = self.mmMemoryManager.getValueFrom(intRightAddrAddr)
                else:
                    # It's directly an address
                    intRightAddress = self.lstlstQuads[intQuadIndex][2]

                # With the right address, we ask for the right value
                rightValue = self.mmMemoryManager.getValueFrom(intRightAddress)

                # We perform the diff
                result = leftValue != rightValue

                # And we save it in the result address
                self.mmMemoryManager.setValue(self.lstlstQuads[intQuadIndex][3], result)

                # Finally, we increment the quad index
                intQuadIndex += 1

            # ----------------------------------------------------------------------------------------------------------
            # Assignment Code
            # ----------------------------------------------------------------------------------------------------------
            elif self.lstlstQuads[intQuadIndex][0] == "=":
                # Execute assignment code
                # Cases:
                # 1. [ = , 100  , None , 200 ]
                # 2. [ = , [100] , None , 200 ]
                # 3. [ = , 100 , None , [200] ]
                # 4. [ = , [100] , None , [200] ]

                # First, we get the value we want to assign
                if isinstance(self.lstlstQuads[intQuadIndex][1], list):
                    # If it's a list, that's an address of an address
                    intResultAddrAddr = self.lstlstQuads[intQuadIndex][1][0]
                    intResultAddress = self.mmMemoryManager.getValueFrom(intResultAddrAddr)
                else:
                    # It's directly an address
                    intResultAddress = self.lstlstQuads[intQuadIndex][1]

                # With the left address, we ask for the left value
                resultValue = self.mmMemoryManager.getValueFrom(intResultAddress)


                # Then, we get address of the assignee
                if isinstance(self.lstlstQuads[intQuadIndex][3], list):
                    # If it's a list, that's an address of an address
                    intAssigneeAddrAddr = self.lstlstQuads[intQuadIndex][3][0]
                    intAssigneeAddress = self.mmMemoryManager.getValueFrom(intAssigneeAddrAddr)
                else:
                    # It's directly an address
                    intAssigneeAddress = self.lstlstQuads[intQuadIndex][3]

                # We perform the assignment
                self.mmMemoryManager.setValue(intAssigneeAddress, resultValue)

                # Finally, we increment the quad index
                intQuadIndex += 1

            # ----------------------------------------------------------------------------------------------------------
            # Graphics Codes
            # ----------------------------------------------------------------------------------------------------------
            elif self.lstlstQuads[intQuadIndex][0] == "circle":
                # Execute assignment code
                # Cases:
                # 1. [ circle , [x, y, radius, color]  , None , None ]


                # First, we get the x coord
                if isinstance(self.lstlstQuads[intQuadIndex][1][0], list):
                    # If it's a list, that's an address of an address
                    intXAddrAddr = self.lstlstQuads[intQuadIndex][1][0][0]
                    intXAddress = self.mmMemoryManager.getValueFrom(intXAddrAddr)
                else:
                    # It's directly an address
                    intXAddress = self.lstlstQuads[intQuadIndex][1][0]

                # With the left address, we ask for the left value
                xValue = self.mmMemoryManager.getValueFrom(intXAddress)

                # Then, we get the y coord
                if isinstance(self.lstlstQuads[intQuadIndex][1][1], list):
                    # If it's a list, that's an address of an address
                    intYAddrAddr = self.lstlstQuads[intQuadIndex][1][1][0]
                    intYAddress = self.mmMemoryManager.getValueFrom(intYAddrAddr)
                else:
                    # It's directly an address
                    intYAddress = self.lstlstQuads[intQuadIndex][1][1]

                # With the left address, we ask for the left value
                yValue = self.mmMemoryManager.getValueFrom(intYAddress)

                # We get the radius coord
                if isinstance(self.lstlstQuads[intQuadIndex][1][2], list):
                    # If it's a list, that's an address of an address
                    intRadiusAddrAddr = self.lstlstQuads[intQuadIndex][1][2][0]
                    intRadiusAddress = self.mmMemoryManager.getValueFrom(intRadiusAddrAddr)
                else:
                    # It's directly an address
                    intRadiusAddress = self.lstlstQuads[intQuadIndex][1][2]

                # With the left address, we ask for the left value
                radiusValue = self.mmMemoryManager.getValueFrom(intRadiusAddress)


                # Color extracted
                color = self.lstlstQuads[intQuadIndex][1][3]


                # We draw the circle
                self.t.setx(xValue)
                self.t.sety(yValue)

                self.t.color(color)

                self.t.begin_fill()

                self.t.pendown()
                self.t.circle(radiusValue)
                self.t.penup()

                self.t.end_fill()

                # Finally, we increment the quad index
                intQuadIndex += 1

            elif self.lstlstQuads[intQuadIndex][0] == "square":
                # Execute assignment code
                # Cases:
                # 1. [ sqiare , [x, y, size, color]  , None , None ]


                # First, we get the x coord
                if isinstance(self.lstlstQuads[intQuadIndex][1][0], list):
                    # If it's a list, that's an address of an address
                    intXAddrAddr = self.lstlstQuads[intQuadIndex][1][0][0]
                    intXAddress = self.mmMemoryManager.getValueFrom(intXAddrAddr)
                else:
                    # It's directly an address
                    intXAddress = self.lstlstQuads[intQuadIndex][1][0]

                # With the left address, we ask for the left value
                xValue = self.mmMemoryManager.getValueFrom(intXAddress)

                # Then, we get the y coord
                if isinstance(self.lstlstQuads[intQuadIndex][1][1], list):
                    # If it's a list, that's an address of an address
                    intYAddrAddr = self.lstlstQuads[intQuadIndex][1][1][0]
                    intYAddress = self.mmMemoryManager.getValueFrom(intYAddrAddr)
                else:
                    # It's directly an address
                    intYAddress = self.lstlstQuads[intQuadIndex][1][1]

                # With the left address, we ask for the left value
                yValue = self.mmMemoryManager.getValueFrom(intYAddress)

                # We get the size
                if isinstance(self.lstlstQuads[intQuadIndex][1][2], list):
                    # If it's a list, that's an address of an address
                    intSizeAddrAddr = self.lstlstQuads[intQuadIndex][1][2][0]
                    intSizeAddress = self.mmMemoryManager.getValueFrom(intSizeAddrAddr)
                else:
                    # It's directly an address
                    intSizeAddress = self.lstlstQuads[intQuadIndex][1][2]

                # With the left address, we ask for the left value
                sizeValue = self.mmMemoryManager.getValueFrom(intSizeAddress)


                # Color extracted
                color = self.lstlstQuads[intQuadIndex][1][3]


                # We draw the circle
                self.t.setx(xValue)
                self.t.sety(yValue)

                self.t.color(color)

                self.t.begin_fill()

                self.t.pendown()
                self.t.forward(sizeValue)
                self.t.left(90)
                self.t.forward(sizeValue)
                self.t.left(90)
                self.t.forward(sizeValue)
                self.t.left(90)
                self.t.forward(sizeValue)
                self.t.left(90)
                self.t.penup()

                self.t.end_fill()

                # Finally, we increment the quad index
                intQuadIndex += 1

            # ----------------------------------------------------------------------------------------------------------
            # No code recognized. It's an error
            else:
                sys.exit("Exit with error: Execution Error\nUnrecognized code '" + self.lstlstQuads[intQuadIndex][0] +
                         "' at the quads.")

        # If we are at debug, we want to also see the memory at the end
        if boolDebugMode:
            self.mmMemoryManager.printMemory()

        turtle.done()

    # ------------------------------------------------------------------------------------------------------------------
    # Error functions
    # ------------------------------------------------------------------------------------------------------------------
    def errorDiv0(self):
        sys.exit("Exit with error: Division by 0 not possible")

    def errorOutOfBounds(self):
        sys.exit("Exit with error: Index out of bounds")