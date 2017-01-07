import Grids as Grids

with open("/Users/markhauenstein/PycharmProjects/SudokuSolver/input.txt", mode='rt') as inputTxt:
    inputArr = inputTxt.readlines()



TL = Grids.Grid(inputArr[0], "Top Left")
TM = Grids.Grid(inputArr[1], "Top Middle")
TR = Grids.Grid(inputArr[2], "Top Right")
ML = Grids.Grid(inputArr[3], "Middle Left")
MM = Grids.Grid(inputArr[4], "Middle Middle")
MR = Grids.Grid(inputArr[5], "Middle Right")
BL = Grids.Grid(inputArr[6], "Bottom Left")
BM = Grids.Grid(inputArr[7], "Bottom Middle")
BR = Grids.Grid(inputArr[8], "Bottom Right")

bigGrid = Grids.BigGrid(TL, TM, TR, ML, MM, MR, BL, BM, BR)







for TL in TL.validGrids:
    for TM in TM.validGrids:
        for TR in TR.validGrids:
            for ML in ML.validGrids:
                for MM in MM.validGrids:
                    for MR in MR.validGrids:
                        for BL in BL.validGrids:
                            for BM in BM.validGrids:
                                for BR in BR.validGrids:
                                    if Grids.BigGrid(TL, TM, TR, ML, MM, MR, BL, BM, BR).allGridsValid:
                                        print((TL.contents, TM.contents, TR.contents, ML.contents, MM.contents, MR.contents, BL.contents, BM.contents, BR.contents))

        # I BET I CAN MAKE THIS MORE EFFICANT IF I SOLVE IT IN CLUSTERS
        # solve for the horizontals, then virticals. should have an answer by ther last iteration

