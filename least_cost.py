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

def getLeastCell(matrix):
    row = 0
    col = 0
    mini = INT_MAX
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <= mini:
                mini = matrix[i][j]
                row = i
                col = j
    return row,col

def makeBothMax(matrix,row,col):
    #eleminate row
    for i in range(len(matrix[row])):
        matrix[row][i] = INT_MAX
    #eleminate col
    for i in range(len(matrix)):
        matrix[i][col] = INT_MAX

def makeRowMax(matrix,row):
    for i in range(len(matrix[row])):
        matrix[row][i] = INT_MAX
def makeColMax(matrix,col):
    for i in range(len(matrix)):
        matrix[i][col] = INT_MAX

matrix = [
    [3,1,7,4],
    [2,6,5,9],
    [8,3,3,2],
]

supply = [300,400,500]
demand = [250,350,400,200]
checkBalanced(matrix,supply,demand)
printMat(matrix)

result = []
while sum(supply)!=0 and sum(demand)!=0:
    row, col = getLeastCell(matrix)
    if supply[row]==demand[col]:
        result.append([matrix[row][col],demand[col]])
        demand[col] = 0
        supply[row] = 0
        makeBothMax(matrix,row,col)
    elif supply[row] > demand[col]:
        result.append([matrix[row][col],demand[col]])
        supply[row] -= demand[col]
        demand[col] = 0
        makeColMax(matrix,col)
    elif supply[row] < demand[col]:
        result.append([matrix[row][col],supply[row]])
        demand[col] -= supply[row]
        supply[row] = 0
        makeRowMax(matrix,row)

print("Allocation->",result)
total = 0
for i in range(len(result)):
    total += (result[i][0]*result[i][1])
print("total cost=",total)
