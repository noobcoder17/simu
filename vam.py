import sys
INT_MAX = sys.maxsize

def printMat(matrix):
    print("Cost Matrix:")
    l = len(matrix)
    for i in range(l):
        print(matrix[i])
def addRow(matrix):
    l = len(matrix[0])
    temp = [0 for _ in range(l)]
    matrix.append(temp)
def addCol(matrix):
    l = len(matrix)
    for i in range(l):
        matrix[i].append(0)

def balance(matrix,supply,demand):
    diff = abs(sum(supply)-sum(demand))
    if(sum(supply)>sum(demand)):
        demand.append(diff)
        addCol(matrix)
    else:
        supply.append(diff)
        addRow(matrix)

def checkBalanced(matrix,supply,demand):
    if(sum(supply)==sum(demand)):
        print("Balanced")
    else:
        print("Not Balanced")
        balance(matrix,supply,demand)
matrix = [
    [3,1,7,4],
    [2,6,5,9],
    [8,3,3,2],
]
supply = [250,350,400]
demand = [200,300,350,150]
checkBalanced(matrix,supply,demand)
#print(supply,demand)
printMat(matrix)

def getRowDiff(matrix,rowDiff):
    for i in range(len(matrix)):
        temp = [matrix[i][col] for col in range(len(matrix[0]))]
        temp.sort()
        diff = temp[1] - temp[0]
        rowDiff[i] = diff

def getColDiff(matrix,colDiff):
    for i in range(len(matrix[0])):
        temp = [matrix[row][i] for row in range(len(matrix))]
        temp.sort()
        diff = temp[1] - temp[0]
        colDiff[i] = diff

result = []
while sum(supply)!=0 and sum(demand)!=0:
    rowDiff = [0 for _ in range(len(matrix))]
    colDiff = [0 for _ in range(len(matrix[0]))]
    getRowDiff(matrix,rowDiff)
    getColDiff(matrix,colDiff)
    #print(rowDiff,colDiff)
    rowDiffMax = max(rowDiff)
    colDiffMax = max(colDiff)

    if rowDiffMax >= colDiffMax:
        row = rowDiff.index(rowDiffMax)
        minInRow = min(matrix[row])
        col = matrix[row].index(minInRow)
    else:
        col = colDiff.index(colDiffMax) 
        temp = [matrix[row][col] for row in range(len(matrix))]
        minInCol = min(temp)
        row = temp.index(minInCol)

    if supply[row] == demand[col]:
            result.append([matrix[row][col],supply[row]])
            supply[row] = 0
            demand[col] = 0
            for i in range(len(matrix[0])):
                matrix[row][i] = INT_MAX
            for i in range(len(matrix)):
                matrix[i][col] = INT_MAX
    elif supply[row] > demand[col]:
        result.append([matrix[row][col],demand[col]])
        supply[row] -= demand[col]
        demand[col] = 0
        for i in range(len(matrix)):
            matrix[i][col] = INT_MAX
    else:
        result.append([matrix[row][col],supply[row]])
        demand[col] -= supply[row]
        supply[row] = 0
        for i in range(len(matrix[0])):
            matrix[row][i] = INT_MAX
    #printMat(matrix)
    #print(supply,demand)

print("Allocation->",result)
total = 0
for i in range(len(result)):
    total += (result[i][0]*result[i][1])
print("total cost=",total)