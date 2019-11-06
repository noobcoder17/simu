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

supply = [300,400,500]
demand = [250,350,400,200]
checkBalanced(matrix,supply,demand)
printMat(matrix)

result = []
row = 0
col = 0
while sum(supply)!=0 and sum(demand)!=0:
    if supply[row]==demand[col]:
        result.append([matrix[row][col],demand[col]])
        demand[col] = 0
        supply[row] = 0
        row += 1
        col += 1
    elif supply[row] > demand[col]:
        result.append([matrix[row][col],demand[col]])
        supply[row] -= demand[col]
        demand[col] = 0
        col += 1
    elif supply[row] < demand[col]:
        result.append([matrix[row][col],supply[row]])
        demand[col] -= supply[row]
        supply[row] = 0
        row += 1

print("Allocation->",result)
total = 0
for i in range(len(result)):
    total += (result[i][0]*result[i][1])
print("total cost=",total)
