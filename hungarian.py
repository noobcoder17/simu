def printMatrix(matrix):
    print("New matrix:")
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")
    
def checkS(matrix):
    if len(matrix) == len(matrix[0]):
        return True
    return False

def rowReduction(matrix):
    for i in range(len(matrix)):
        minInRow = min(matrix[i])
        for j in range(len(matrix[i])):
            matrix[i][j]-=minInRow
    printMatrix(matrix)

def columnReduction(matrix):
    for i in range(len(matrix[0])):
        temp = [matrix[j][i] for j in range(len(matrix))]
        minInCol = min(temp)
        if minInCol!=0:
            for j in range(len(matrix)):
                matrix[j][i]-=minInCol
    printMatrix(matrix)

def degeneracy(matrix):
    zeroInRow = []
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                count+=1
        zeroInRow.append(count)
    zeroInCol = []
    for i in range(len(matrix[0])):
        count = 0
        temp = [matrix[j][i] for j in range(len(matrix))]
        for j in range(len(temp)):
            if temp[j]==0:
                count+=1
        zeroInCol.append(count)
    print(zeroInRow)
    print(zeroInCol)
    horizontalLines = []
    verticalLines = []
    letsGo =True
    while letsGo:
        if max(zeroInRow)>=max(zeroInCol):
            maxZeroRow = zeroInRow.index(max(zeroInRow))
            zeroInRow[maxZeroRow] = 0
            horizontalLines.append(maxZeroRow)
            for j in range(len(matrix[maxZeroRow])):
                if matrix[maxZeroRow][j] == 0:
                    zeroInCol[j] -=1
        else:
            maxZeroCol = zeroInCol.index(max(zeroInCol))
            zeroInCol[maxZeroCol] = 0
            verticalLines.append(maxZeroCol)
            for j in range(len(matrix)):
                if matrix[j][maxZeroCol] == 0:
                    zeroInRow[j] -=1
        if sum(zeroInRow)+sum(zeroInCol)==0:
            letsGo = False
    print(horizontalLines)
    print(verticalLines)
    if len(horizontalLines)+len(verticalLines) < len(matrix):
        return False,horizontalLines,verticalLines
    else:
        return True,horizontalLines,verticalLines



# def degeneracy(matrix):
#     cells = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j]==0:
#                 cells.append([i,j])

#     for cell in cells:
#         #for row of that cell
#         row = cell[0]
        

def solveHungarian(matrix):
    if checkS(matrix):
        rowReduction(matrix)
        columnReduction(matrix)
        isdegen, hoLines, verLInes = degeneracy(matrix)
        if isdegen==False:
            temp = []
            for i in range(len(matrix)):
                if i not in hoLines:
                    for j in range(len(matrix[0])):
                        if j not in verLInes:
                            temp.append()





matrix = [
    [9, 11, 14, 11, 7],
    [6, 15, 13, 13, 10],
    [12, 13, 6, 8, 8],
    [11, 9, 10, 12, 9],
    [7, 12, 14, 10, 14]
]
solveHungarian(matrix)