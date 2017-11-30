from Virtual_Memory.GlobalMemoryBlock import GlobalMemoryBlock
from Virtual_Memory.LocalMemoryBlock import LocalMemoryBlock
import sys

class MemoryManager:

    def __init__(self, gmbGlobal):
        self.gmbGlobal = gmbGlobal

        self.intGlobalDirBase = self.gmbGlobal.intDirBase
        self.intLocalDirBase = self.gmbGlobal.intDirBase + self.gmbGlobal.intMAX_BLOCK_SIZE

        self.stkExecutionBlocks = [LocalMemoryBlock(self.intLocalDirBase)]

    def addNewContext(self):
        self.stkExecutionBlocks.append(LocalMemoryBlock(self.intLocalDirBase))

    def deleteCurrentContext(self):
        self.stkExecutionBlocks.pop()

    def getValueFrom(self, intAddress):

        # We check where in which Memory Block it falls
        if self.intGlobalDirBase <= intAddress < self.intLocalDirBase:
            # Global Memory Block Range
            return self.gmbGlobal.getValue(intAddress)
        elif self.intLocalDirBase <= intAddress < self.intLocalDirBase + self.stkExecutionBlocks[-1].intMAX_BLOCK_SIZE:
            # Local Memory Block Range
            return self.stkExecutionBlocks[-1].getValue(intAddress)
        else:
            sys.exit("Exit with error: Trying to access a nonexistent address while getting a value at MemoryManager")

    def setValue(self, intAddress, obiValue):
        # We check where in which Memory Block it falls
        if self.intGlobalDirBase <= intAddress < self.intLocalDirBase:
            # Global Memory Block Range
            self.gmbGlobal.setValue(intAddress, obiValue)
        elif self.intLocalDirBase <= intAddress < self.intLocalDirBase + self.stkExecutionBlocks[-1].intMAX_BLOCK_SIZE:
            # Local Memory Block Range
            self.stkExecutionBlocks[-1].setValue(intAddress, obiValue)
        else:
            sys.exit("Exit with error: Trying to access a nonexistent address while getting a value at MemoryManager")

    # Prints all the memory blocks within the memory manager
    def printMemory(self):
        print("=======================================================")
        print("Global Memory")
        self.gmbGlobal.printMemory()

        print("=======================================================")
        print("Local Contexts")

        for lmbContext in self.stkExecutionBlocks:
            lmbContext.printMemory()
