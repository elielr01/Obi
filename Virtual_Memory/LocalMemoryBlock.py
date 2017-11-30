# -*- coding: utf-8 -*-
#
# Obi - LocalMemoryBlock
#
# Class that represents the local memory needed for the local functions (play included). Each block is independent
# and there should be 1 block per function in a program
#
# Author: Elí E. Linares
# ID: A00815654
# Date: Nov 27, 2017

import sys
from MemorySegment import MemorySegment

class LocalMemoryBlock:

    # Constructor
    def __init__(self, intDirBase):

        # Base Address of the block
        self.intDirBase = intDirBase

        # Constants for a Local Block
        self.intMAX_SEGMENT_SIZE = 40000
        self.intMAX_BLOCK_SIZE = self.intMAX_SEGMENT_SIZE * 2

        # Base addresses for each memory segment
        self.intLocalDirBase = intDirBase
        self.intTemporalLocalDirBase = intDirBase + self.intMAX_SEGMENT_SIZE

        # We initialize both memory segments with their corresponding base addresses and max sizes
        self.msLocal = MemorySegment(self.intLocalDirBase, self.intMAX_SEGMENT_SIZE)
        self.msTemporalLocal = MemorySegment(self.intTemporalLocalDirBase, self.intMAX_SEGMENT_SIZE)

    # Returns the next available local address
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

    # Returns the next available temporal local address
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

    # Returns the needed size of the block. This represents the size of a function
    def intGetBlockNeededSize(self):
        return self.msLocal.intGetNeededSize() + self.msTemporalLocal.intGetNeededSize()

    # Returns a value according to the given memory address
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

    # Sets a value to a memory address
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

    # Resets the pointers when a new local context is created
    def reset(self):
        self.msLocal.resetPointers()
        self.msTemporalLocal.resetPointers()

    def printMemory(self):
        print("--------------------------------------------------------")
        print("Local Memory")
        self.msLocal.printSegment()

        print("--------------------------------------------------------")
        print("Local Temporal Memory")
        self.msTemporalLocal.printSegment()

