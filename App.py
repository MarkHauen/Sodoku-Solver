import Grids as Grids

with open("/*******PATH*******/SudokuSolver/input.txt", mode='rt') as input:
    inputArr = input.readlines()

with open("/*******PATH*******/SudokuSolver/allPossibles.txt", mode='rt') as allPossibles:
    allValids = allPossibles.readlines()

TL = Grids.Grid(inputArr[0])
TM = Grids.Grid(inputArr[1])
TR = Grids.Grid(inputArr[2])
ML = Grids.Grid(inputArr[3])
MM = Grids.Grid(inputArr[4])
MR = Grids.Grid(inputArr[5])
BL = Grids.Grid(inputArr[6])
BM = Grids.Grid(inputArr[7])
BR = Grids.Grid(inputArr[8])

bigGrid = Grids.BigGrid(TL, TM, TR, ML, MM, MR, BL, BM, BR)


def findPossibles(gameGrid):
    print("Finding possibles for", gameGrid)
    possiblesList = []
    goal = len(gameGrid.immutableIndexs)
    for possibles in allValids:
        possibleGrid = Grids.Grid(possibles)
        counter = 0
        for immutableIndex in gameGrid.immutableIndexs:
            if immutableIndex[0] == possibleGrid.contents[immutableIndex[1]]:
                counter += 1
        if counter == goal:
            possiblesList.append(possibleGrid)
    return possiblesList

TLpossibles = findPossibles(TL)
TMpossibles = findPossibles(TM)
TRpossibles = findPossibles(TR)
MLpossibles = findPossibles(ML)
MMpossibles = findPossibles(MM)
MRpossibles = findPossibles(MR)
BLpossibles = findPossibles(BL)
BMpossibles = findPossibles(BM)
BRpossibles = findPossibles(BR)

listOfListsOfPossibles = [TLpossibles,TMpossibles,TRpossibles,MLpossibles,MMpossibles,MRpossibles,BLpossibles,BMpossibles,BRpossibles]


for TL in TLpossibles:
    for TM in TMpossibles:
        for TR in TRpossibles:
            for ML in MLpossibles:
                for MM in MMpossibles:
                    for MR in MRpossibles:
                        for BL in BLpossibles:
                            for BM in BMpossibles:
                                for BR in BRpossibles:
                                    if Grids.BigGrid(TL, TM, TR, ML, MM, MR, BL, BM, BR).allGridsValid:
                                        print((TL.contents, TM.contents, TR.contents, ML.contents, MM.contents, MR.contents, BL.contents, BM.contents, BR.contents))

