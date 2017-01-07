import Grids as Grids

def allPossibleGrids():
    allPossiblestxt = open("/Users/markhauenstein/PycharmProjects/SudokuSolver/allPossibles.txt", mode='w')
    validGrids = []
    i = 0
    for TL in range(1, 10):
        for TM in range(1, 10):
            for TR in range(1, 10):
                for ML in range(1, 10):
                    for MM in range(1, 10):
                        for MR in range(1, 10):
                            for BL in range(1, 10):
                                for BM in range(1, 10):
                                    for BR in range(1, 10):
                                        i += 1
                                        if Grids.Grid(TL, TM, TR, ML, MM, MR, BL, BM, BR).isValid:
                                            print(i, "|||", TL, TM, TR, ML, MM, MR, BL, BM, BR)
                                            validGrids.append(Grids.Grid(TL, TM, TR, ML, MM, MR, BL, BM, BR))
                                            allPossiblestxt.write(str(TL) + str(TM) + str(TR) + str(ML) + str(MM) + str(MR) + str(BL) + str(BM) + str(BR)+"\n")
    allPossiblestxt.close()
    return validGrids

with open("/Users/markhauenstein/PycharmProjects/SudokuSolver/allPossibles.txt", mode='rt') as allPossibles:
    allValids = allPossibles.readlines()