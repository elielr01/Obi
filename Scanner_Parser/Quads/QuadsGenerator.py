

class QuadsGenerator:

    def __init__(self):
        self.dicttplQuads = {}
        self.intQuadsCont = 0

    def addQuad(self, tplQuadTuple):
        self.intQuadsCont += 1
        self.dicttplQuads[self.intQuadsCont] = tplQuadTuple


    def printQuads(self):
        for (key, value) in self.dicttplQuads.items():
            print(str(key) + ". " + str(value))
