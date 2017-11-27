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

            if self.lstlstQuads[intQuadIndex][0] == "Print":
                #execute print code
                print(self.mmMemoryManager.getValueFrom(self.lstlstQuads[intQuadIndex][3]))
                intQuadIndex += 1
            elif self.lstlstQuads[intQuadIndex][0] == "GoTo":
                # Execute a Jump
                intQuadIndex = self.lstlstQuads[intQuadIndex][3]

    # ------------------------------------------------------------------------------------------------------------------
    # Error functions
    # ------------------------------------------------------------------------------------------------------------------
    def errorDiv0(self):
        sys.exit("Exit with error: Division by 0 not possible")

    def errorOutOfBounds(self):
        sys.exit("Exit with error: Index out of bounds")