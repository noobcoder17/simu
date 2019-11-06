cj = [4,3,0,0,0,0]
var = ['x1','x2']
basicVar = ['x1','x2','s1','s2','s3','s4','sol']
cbj = {
    0:'s1',
    1:'s2',
    2:'s3',
    3:'s4'
}
cbjVal = [0,0,0,0]
ratio = [0,0,0,0]
main = [
    [2,1,1,0,0,0,1000],
    [1,1,0,1,0,0,800],
    [1,0,0,0,1,0,400],
    [0,1,0,0,0,1,700],
]


zj = [0,0,0,0,0,0,0]
cjzj = [0,0,0,0,0,0]

problemType = 'max'

if problemType == 'max':
   for i in range(len(cjzj)):
       cjzj[i] = 9999 
else:
    for i in range(len(cjzj)):
       cjzj[i] = -9999

def printAll():
    print("\n_____________________________")
    print("CBj:",cbj)
    print("CBj value:",cbjVal)
    print("\nMain list:")
    for i in range(len(main)):
        print(main[i][:-1])
    print("\nSolution:",[main[i][-1] for i in range(len(main))])
    #print("Ratio:",ratio)
    print("Zj:",zj)
    print("Cj-Zj:",cjzj) 
    print("_____________________________\n")


def makeNewTable(row,col):
    tempTable = []
    for i in range(len(main)):
        tempTable.append([i for i in main[i]])
    print()
    print("key Element:",main[row][col])
    print("leaving variable:",cbj[row])
    print("Entering variable:",basicVar[col])
    cbj[row] = basicVar[col]
    cbjVal[row] = cj[col]
    keyElement = main[row][col]
    for i in range(len(basicVar)):
        main[row][i] = main[row][i]/keyElement
    
    for currRow in range(len(main)):
        if currRow != row:
            for currCol in range(len(basicVar)):
                #print(main[currRow][col])
                val = main[currRow][currCol] - (
                    (tempTable[currRow][col]*tempTable[row][currCol])/keyElement
                )
                if val > 0 and val < 0.001:
                    print("For-",val,currRow,currCol)
                    main[currRow][currCol] = 0
                else:
                     main[currRow][currCol] = val

def calZj():
    for i in range(len(basicVar)):
        total = 0
        for j in range(len(cbjVal)):
            total += cbjVal[j]*main[j][i]
        zj[i] = total

def calCjZj():
    for i in range(len(basicVar)-1):
        cjzj[i] = cj[i] - zj[i]
def calCutaleRatio(col):
    for i in range(len(ratio)):
        if main[i][col] <=0:
            ratio[i] = 9999    
        else:
            ratio[i] = main[i][-1]/main[i][col]


print("Initial simple table:")
calZj()
calCjZj()
printAll()

def check(cjzj):
    for i in cjzj:
        if i > 0:
            return True
    return False

iteretion = 1
if problemType == 'max':
    while check(cjzj):
        print("iteration-",iteretion)
        iteretion+=1
        #print("Sum of Cj - Zj:",sum(cjzj))
        maxOfcjzj = max(cjzj)
        col = cjzj.index(maxOfcjzj)
        calCutaleRatio(col)
        print("Ratio:",ratio)
        minOfratio = min(ratio)
        print("Min of ratio:",minOfratio)
        row = ratio.index(minOfratio)
        print("Row,Col-",[row,col])
        makeNewTable(row,col)
        calZj()
        calCjZj()
        printAll()
    
    print("So the maximum value of Z=",zj[-1])
    indexes = []
    z = [main[i][-1] for i in range(len(main))]
    sol = {}
    for key in cbj.keys():
        if cbj[key] in var:
            if cbj[key] not in sol.keys():
                sol[cbj[key]] = z[key]

    print("The solution is:",sol)
