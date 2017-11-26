import sys
from MemorySegment import MemorySegment

class LocalMemoryBlock:

    def __init__(self, intDirBase):

        self.intDirBase = intDirBase

        self.intMAX_SEGMENT_SIZE = 40000
        self.intMAX_BLOCK_SIZE = self.intMAX_SEGMENT_SIZE * 2

        self.intLocalDirBase = intDirBase
        self.intTemporalLocalDirBase = intDirBase + self.intMAX_SEGMENT_SIZE

        self.msLocal = MemorySegment(self.intLocalDirBase, self.intMAX_SEGMENT_SIZE)
        self.msTemporalLocal = MemorySegment(self.intTemporalLocalDirBase, self.intMAX_SEGMENT_SIZE)

    def intNextLocalAddress(self, strType):
        # We check which type is needed
        if strType == "Int":
            return self.msLocal.intNextIntAddress()
        elif strType == "Float":
            return self.msLocal.intNextFloatAddress()
        elif strType == "Bool":
            return self.msLocal.intNextBoolAddress()
        elif strType == "String":
            return self.msLocal.intNextStrAddress()
        else:
            sys.exit("Exit with error: Type not valid while getting an address at Local Memory")

    def intNextTemporalLocalAddress(self, strType):
        # We check which type is needed
        if strType == "Int":
            return self.msTemporalLocal.intNextIntAddress()
        elif strType == "Float":
            return self.msTemporalLocal.intNextFloatAddress()
        elif strType == "Bool":
            return self.msTemporalLocal.intNextBoolAddress()
        elif strType == "String":
            return self.msTemporalLocal.intNextStrAddress()
        else:
            sys.exit("Exit with error: Type not valid while getting an address at Temporal Local Memory")

    def intGetBlockNeededSize(self):
        return self.msLocal.intGetNeededSize() + self.msTemporalLocal.intGetNeededSize()

    def getValue(self, intAddress):
        #Check what kind of memory it is
        if self.intLocalDirBase <= intAddress < self.intTemporalLocalDirBase:
            #Local memory range
            return self.msLocal.getValue(intAddress)
        elif self.intTemporalLocalDirBase <= intAddress < (self.intTemporalLocalDirBase + self.intMAX_SEGMENT_SIZE):
            #Temporal local memory range
            return self.msTemporalLocal.getValue(intAddress)
        else:
            sys.exit("Exit with error: Trying to accessing an address out of context while getting value at Local Memory Block")

    def setValue(self, intAddress, obiValue):
        # Check what kind of memory it is
        if self.intLocalDirBase <= intAddress < self.intTemporalLocalDirBase:
            # Local memory range
            self.msLocal.setValue(intAddress, obiValue)
        elif self.intTemporalLocalDirBase <= intAddress < (self.intTemporalLocalDirBase + self.intMAX_SEGMENT_SIZE):
            # Temporal local memory range
            self.msTemporalLocal.setValue(intAddress, obiValue)
        else:
            sys.exit("Exit with error: Trying to accessing an address out of context while setting value at Local Memory Block")
