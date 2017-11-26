import sys

class MemorySegment:

    def __init__(self, intDirBase, intMaxSize):

        self.intTypeSegmentSize = intMaxSize / 4

        self.intIntsDirBase = self.intIntsPointer = intDirBase #5,000
        self.intFloatsDirBase = self.intFloatsPointer = intDirBase + self.intTypeSegmentSize #15,000
        self.intBoolsDirBase = self.intBoolsPointer = intDirBase + self.intTypeSegmentSize * 2 #25,000
        self.intStrsDirBase = self.intStrsPointer = intDirBase + self.intTypeSegmentSize * 3 #35,000

        self.dictintInts = {} #5,000 - 14,999
        self.dictftsFloats = {} #15,000 - 24,999
        self.dictboolBools = {} #25,000 - 34,999
        self.dictstrStrings = {} #35,000 - 44,999

        self.intDirBase = intDirBase #5,000
        self.intMaxSize = intMaxSize #40,000

    # Returns the next available space for each type

    def intNextIntAddress(self):
        intNextFreeInt = self.intIntsPointer
        self.intIntsPointer += 1
        return intNextFreeInt

    def intNextFloatAddress(self):
        intNextFreeFloat = self.intFloatsPointer
        self.intFloatsPointer += 1
        return intNextFreeFloat

    def intNextBoolAddress(self):
        intNextFreeBool = self.intBoolsPointer
        self.intBoolsPointer += 1
        return intNextFreeBool

    def intNextStrAddress(self):
        intNextFreeString = self.intStrsPointer
        self.intStrsPointer += 1
        return intNextFreeString

    # Get a value for a given address

    def getValue(self, intAddress):
        # We check in which range it falls
        if (self.intIntsDirBase <= intAddress and
            intAddress < self.intFloatsDirBase and
            intAddress in self.dictintInts):
            # Ints Range and the value exists
            return self.dictintInts[intAddress]
        elif (self.intFloatsDirBase <= intAddress and
            intAddress < self.intBoolsDirBase and
            intAddress in self.dictftsFloats):
            # Floats Range and the value exists
            return self.dictftsFloats[intAddress]
        elif (self.intBoolsDirBase <= intAddress and
            intAddress < self.intStrsDirBase and
            intAddress in self.dictboolBools):
            # Bools Range
            return self.dictboolBools[intAddress]
        elif (self.intStrsDirBase <= intAddress and
            intAddress < (self.intStrsDirBase + self.intTypeSegmentSize) and
            intAddress in self.dictstrStrings):
            # Strings Range
            return self.dictstrStrings[intAddress]
        else:
            sys.exit("Exit with error: Trying to access a nonexistent address while getting a value.")

    # Add value depending of the type

    def setValue(self, intAddress, obiValue):
        # We check in which range it falls
        if self.intIntsDirBase <= intAddress < self.intFloatsDirBase:
            # Ints Range and the value exists
            self.dictintInts[intAddress] = obiValue
        elif self.intFloatsDirBase <= intAddress < self.intBoolsDirBase:
            # Floats Range and the value exists
            self.dictftsFloats[intAddress] = obiValue
        elif self.intBoolsDirBase <= intAddress < self.intStrsDirBase:
            # Bools Range
            self.dictboolBools[intAddress] = obiValue
        elif self.intStrsDirBase <= intAddress < (self.intStrsDirBase + self.intTypeSegmentSize):
            # Strings Range
            self.dictstrStrings[intAddress] = obiValue
        else:
            sys.exit("Exit with error: Trying to access a nonexistent address while getting a value.")

    def intGetNeededInts(self):
        return self.intIntsPointer - self.intStrsDirBase

    def intGetNeededFloats(self):
        return self.intFloatsPointer - self.intFloatsDirBase

    def intGetNeededBools(self):
        return self.intBoolsPointer - self.intBoolsDirBase

    def intGetNeededStrings(self):
        return self.intStrsPointer - self.intStrsDirBase

    def intGetNeededSize(self):
        return self.intGetNeededInts() + self.intGetNeededFloats() + self.intGetNeededBools() + self.intGetNeededStrings()

    def intGetRealSize(self):
        return len(self.dictintInts) + len(self.dictftsFloats) + len(self.dictboolBools) + len(self.dictstrStrings)


    def printSegment(self):

        print("-----------------------------")
        print("Segment info:")
        print("-----------------------------")
        print("Base Address: " + str(self.intDirBase))
        print("Size: " + str(self.intGetRealSize()))
        print("Max Size: " + str(self.intMaxSize))
        print("")

        print("-----------------------------")
        print("Actual pointers states:")
        print("-----------------------------")
        print("Ints pointer: " + str(self.intIntsPointer))
        print("Floats pointer: " + str(self.intFloatsPointer))
        print("Bools pointer: " + str(self.intBoolsPointer))
        print("Strings pointer: " + str(self.intStrsPointer))
        print("")

        print("-----------------------------")
        print("Ints within memory segment")
        print("-----------------------------")
        for key, value in self.dictintInts:
            print(str(key) + ": " + str(value))

        print("-----------------------------")
        print("Floats within memory segment")
        print("-----------------------------")
        for key, value in self.dictftsFloats:
            print(str(key) + ": " + str(value))

        print("-----------------------------")
        print("Bools within memory segment")
        print("-----------------------------")
        for key, value in self.dictboolBools:
            print(str(key) + ": " + str(value))

        print("-----------------------------")
        print("Strings within memory segment")
        print("-----------------------------")
        for key, value in self.dictstrStrings:
            print(str(key) + ": " + str(value))