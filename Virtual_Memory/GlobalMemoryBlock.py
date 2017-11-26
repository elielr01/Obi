import sys
from MemorySegment import MemorySegment

class GlobalMemoryBlock:

    def __init__(self, intDirBase):

        self.intDirBase = intDirBase

        self.intMAX_SEGMENT_SIZE = 40000
        self.intMAX_BLOCK_SIZE = self.intMAX_SEGMENT_SIZE * 3

        self.intGlobalDirBase = intDirBase
        self.intTemporalGlobalDirBase = intDirBase + self.intMAX_SEGMENT_SIZE
        self.intConstantGlobalDirBase = intDirBase + 2 * self.intMAX_SEGMENT_SIZE

        self.msGlobal = MemorySegment(self.intGlobalDirBase, self.intMAX_SEGMENT_SIZE)
        self.msTemporalGlobal = MemorySegment(self.intTemporalGlobalDirBase, self.intMAX_SEGMENT_SIZE)
        self.msConstantGlobal = MemorySegment(self.intConstantGlobalDirBase, self.intMAX_SEGMENT_SIZE)

    def intNextGlobalAddress(self, strType):
        # We check which type is needed
        if strType == "Int":
            return self.msGlobal.intNextIntAddress()
        elif strType == "Float":
            return self.msGlobal.intNextFloatAddress()
        elif strType == "Bool":
            return self.msGlobal.intNextBoolAddress()
        elif strType == "String":
            return self.msGlobal.intNextStrAddress()
        else:
            sys.exit("Exit with error: Type not valid while getting an address at Global Memory")

    def intNextTemporalGlobalAddress(self, strType):
        # We check which type is needed
        if strType == "Int":
            return self.msTemporalGlobal.intNextIntAddress()
        elif strType == "Float":
            return self.msTemporalGlobal.intNextFloatAddress()
        elif strType == "Bool":
            return self.msTemporalGlobal.intNextBoolAddress()
        elif strType == "String":
            return self.msTemporalGlobal.intNextStrAddress()
        else:
            sys.exit("Exit with error: Type not valid while getting an address at Temporal Global Memory")

    def intNextConstantGlobalAddress(self, strType):
        # We check which type is needed
        if strType == "Int":
            return self.msConstantGlobal.intNextIntAddress()
        elif strType == "Float":
            return self.msConstantGlobal.intNextFloatAddress()
        elif strType == "Bool":
            return self.msConstantGlobal.intNextBoolAddress()
        elif strType == "String":
            return self.msConstantGlobal.intNextStrAddress()
        else:
            sys.exit("Exit with error: Type not valid while getting an address at Constant Global Memory")


    def intGetBlockNeededSize(self):
        return self.msGlobal.intGetNeededSize() + self.msTemporalGlobal.intGetNeededSize() + self.msConstantGlobal.intGetNeededSize()

    def getValue(self, intAddress):
        # Check what kind of memory it is
        if self.intGlobalDirBase <= intAddress < self.intTemporalGlobalDirBase:
            # Global memory range
            return self.msGlobal.getValue(intAddress)
        elif self.intTemporalGlobalDirBase <= intAddress < self.intConstantGlobalDirBase:
            # Temporal global memory range
            return self.msTemporalGlobal.getValue(intAddress)
        elif self.intConstantGlobalDirBase <= intAddress < (self.intConstantGlobalDirBase + self.intMAX_SEGMENT_SIZE):
            # Constant global memory range
            return self.msConstantGlobal.getValue(intAddress)
        else:
            sys.exit("Exit with error: Trying to accessing an address out of context while getting value at Global Memory Block")

    def setValue(self, intAddress, obiValue):
        # Check what kind of memory it is
        if self.intGlobalDirBase <= intAddress < self.intTemporalGlobalDirBase:
            # Global memory range
            self.msGlobal.setValue(intAddress, obiValue)
        elif self.intTemporalGlobalDirBase <= intAddress < self.intConstantGlobalDirBase:
            # Temporal global memory range
            self.msTemporalGlobal.setValue(intAddress, obiValue)
        elif self.intConstantGlobalDirBase <= intAddress < (self.intConstantGlobalDirBase + self.intMAX_SEGMENT_SIZE):
            # Constant global memory range
            self.msConstantGlobal.setValue(intAddress, obiValue)
        else:
            sys.exit("Exit with error: Trying to accessing an address out of context while getting value at Global Memory Block")