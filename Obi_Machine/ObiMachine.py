import sys
from Virtual_Memory.MemoryManager import MemoryManager

class ObiMachine:

    def __init__(self, lstlstQuads, gmbGlobal, ftFuncsTable):

        self.lstlstQuads = lstlstQuads
        self.mmMemoryManager = MemoryManager(gmbGlobal)
        self.ftFuncsTable = ftFuncsTable



    def execute(self):

        intQuadIndex = 1
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
            # No code recognized. It's an error
            else:
                sys.exit("Exit with error: Execution Error\nUnrecognized code '" + self.lstlstQuads[intQuadIndex][0] +
                         "' at the quads.")

    # ------------------------------------------------------------------------------------------------------------------
    # Error functions
    # ------------------------------------------------------------------------------------------------------------------
    def errorDiv0(self):
        sys.exit("Exit with error: Division by 0 not possible")

    def errorOutOfBounds(self):
        sys.exit("Exit with error: Index out of bounds")