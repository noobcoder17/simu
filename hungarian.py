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




#new 
def reduce_row_column(mat,m,n):
    for i in range(m):
        k=min(mat[i])
        if(k!=0):
            for j in range(n):
                mat[i][j]-=k
    for j in range(n):
        k=mat[0][j]
        for i in range(1,m):
            if(k>mat[i][j]):
                k=mat[i][j]
        for i in range(m):
            mat[i][j]-=k

def check_degeneracy(mat,m,n):
    num_of_lines=0
    rows=[False]*m
    cols=[False]*n
    temp=[]
    for i in range(m):
        for j in range(n):
            if(mat[i][j]==0):
                temp.append([i,j])
    for k in temp:
        i,j=k[0],k[1]
        if(rows[i] or cols[j]): continue
        count_r,count_c=0,0
        for p in range(5):
            if(mat[p][j]==0): count_c+=1
            if(mat[i][p]==0): count_r+=1
        if(count_r>=count_c): rows[i]=True
        else: cols[j]=True
        num_of_lines+=1
    return num_of_lines,rows,cols

def modify_matrix(mat,m,n,rows,cols):
    k=1000000009
    for i in range(m):
        for j in range(n):
            if(rows[i] or cols[j]): continue
            if(mat[i][j]<k): k=mat[i][j]
    for i in range(m):
        for j in range(n):
            if(rows[i]==True and cols[j]==True): mat[i][j]+=k
            if(rows[i]==False and cols[j]==False ): mat[i][j]-=k

arr=[[9,11,14,11,7],[6,15,13,13,10],[12,13,6,8,8],[11,9,10,12,9],[7,12,14,10,14]]
mat=[[9,11,14,11,7],[6,15,13,13,10],[12,13,6,8,8],[11,9,10,12,9],[7,12,14,10,14]]
m,n=5,5

while(True):
    reduce_row_column(mat,m,n)
    lines,rows,cols=check_degeneracy(mat,m,n)
    if(lines>=5): break
    modify_matrix(mat,m,n,rows,cols)


row=[0]*m
col=[0]*n
for i in range(m):
    for j in range(n):
        if(mat[i][j]==0):
            row[i]+=1
            col[j]+=1

#print(row,col)
assigned=[False]*m
r=[False]*m
cost=0
for i in range(m):
    for j in range(n):
        if(row[i]==1 and col[j]==1 and mat[i][j]==0):
            print(str(j+1),"assigned to",str(i+1))
            cost+=arr[i][j]
            assigned[j]=True

for j in range(n):
    if(assigned[j]):continue
    for i in range(m):
        if(mat[i][j]==0 and r[i]==False):
            print(str(j+1),"assigned to",str(i+1))
            r[i]=True
            cost+=arr[i][j]
            assigned[j]=True
            break
print(cost)
