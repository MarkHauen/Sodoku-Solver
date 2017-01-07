def checkifValid(contents):
    if contents.__contains__(1) & contents.__contains__(2) & contents.__contains__(3) & contents.__contains__(4) & contents.__contains__(5) & contents.__contains__(6) & contents.__contains__(7) & contents.__contains__(8) & contents.__contains__(9):
        return True


def findImmutableIndexs(contents):
    immutableIndexes = []
    for index in range(0,9):
        if contents[index] != 0:
            immutableIndexes.append((contents[index], index))
    return immutableIndexes



class Grid:
    def __init__(self, textIput):
        self.TL = int(textIput[0])
        self.TM = int(textIput[1])
        self.TR = int(textIput[2])
        self.ML = int(textIput[3])
        self.MM = int(textIput[4])
        self.MR = int(textIput[5])
        self.BL = int(textIput[6])
        self.BM = int(textIput[7])
        self.BR = int(textIput[8])
        self.topH = [self.TL, self.TM, self.TR]
        self.midH = [self.ML, self.MM, self.MR]
        self.botH = [self.BL, self.BM, self.BR]
        self.leftV = [self.TL,self. ML, self.BL]
        self.midV = [self.TM, self.MM, self.BM]
        self.rightV = [self.TR, self.MR, self.BR]
        self.contents = [self.TL, self.TM, self.TR, self.ML, self.MM, self.MR, self.BL, self.BM, self.BR]
        self.isValid = checkifValid(self.contents)
        self.immutableIndexs = findImmutableIndexs(self.contents)


def checkifAllVaild(contents):
    allValid = True
    for grid in contents:
        if not grid.isValid:
            allValid = False
    return allValid


class BigGrid:
    def __init__(self, TL, TM, TR, ML, MM, MR, BL, BM, BR):
        self.topH = Grid(str(TL.TL) + str(TL.TM) + str(TL.TR) + str(TM.TL) + str(TM.TM) + str(TM.TR) + str(TR.TL) + str(TR.TM) + str(TR.TR))
        self.midH = Grid(str(ML.ML) + str(ML.MM) + str(ML.MR) + str(MM.ML) + str(MM.MM) + str(MM.MR) + str(MR.ML) + str(MR.MM) + str(MR.MR))
        self.botH = Grid(str(BL.BL) + str(BL.BM) + str(BL.BR) + str(BM.BL) + str(BM.BM) + str(BM.BR) + str(BR.BL) + str(BR.BM) + str(BR.BR))
        self.leftV = Grid(str(TL.TL) + str(TL.ML) + str(TL.BL) + str(ML.TL) + str(ML.ML) + str(ML.BL) + str(BL.TL) + str(BL.ML) + str(BL.BL))
        self.midV = Grid(str(TM.TM) + str(TM.MM) + str(TM.BM) + str(MM.TM) + str(MM.MM) + str(MM.BM) + str(BM.TM) + str(BM.MM) + str(BM.BM))
        self.rightV = Grid(str(TR.TR) + str(TR.MR) + str(TR.BR) + str(MR.TR) + str(MR.MR) + str(MR.BR) + str(BR.TR) + str(BR.MR) + str(BR.BR))
        self.contents = [self.topH, self.midH, self.botH, self.leftV, self.midV, self.rightV]
        self.allGridsValid = checkifAllVaild(self.contents)
