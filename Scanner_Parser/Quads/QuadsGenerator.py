

class QuadsGenerator:

    def __init__(self):
        self.dictlstQuads = {}
        self.intQuadsCont = 1

    def addQuad(self, lstQuadTuple):
        self.dictlstQuads[self.intQuadsCont] = lstQuadTuple
        intCreatedQuad = self.intQuadsCont
        self.intQuadsCont += 1
        return intCreatedQuad

    def fillQuad(self, intQuadNum):
        self.dictlstQuads[intQuadNum][3] = self.intQuadsCont


    def printQuads(self):
        for (key, value) in self.dictlstQuads.items():
            print(str(key) + ". " + str(value))

    def getQuads(self):
        return self.dictlstQuads.values()