import matplotlib.pyplot as plt  

def join(stuff):
    thingy = ''.join(stuff)
    return thingy

matrix =[]

def constructOperationsMatrix(n):
    submatrix = []
    nTest = None #Binary counting number
    nLen = len(str(n)) #Length of n
    nBin = int(bin(2**(nLen-2)),2) # 
    for i in range(0,2**(nLen-2)):
    
        if nTest == None:#Only does this once
            nTest = nBin
        nCut = str(bin(nTest)).replace('0b1','')#Replaces binary ID of string so we just get the 1's and 0's.
        nCutList = list(nCut) #Turns the string of 1s and 0s into a list

        for i in range(len(nCut)):#Swaps + for 1, - for 0

            if nCutList[i] == '1':
                nCutList[i] = '+'
            elif nCutList[i] == '0':
                nCutList[i] = '-'
        for i in range(len(nCutList)+1):
            submatrix.append(nCutList[:])
        nTest = nTest + 1
    for i in range(0,(len(nCutList)+1)*(2**(nLen-2))):
        submatrix[i].insert((i % (len(nCutList)+1)),'==')
    return submatrix
#Test if given number is good or bad
def testGoodBad(n): #input is any integer greater than 100
    nMatrix = constructOperationsMatrix(n)
    nList = list(str(n))
    nEqn = []
    testingList = []
    #this is what gets a number, splices it, inserts the operations, rejoins it, and evaluates it
    for z in nMatrix:
        nOps = z
        nSubList = list(str(n))
        
        for i in range(len(nOps)):
            nSubList.insert((i*2+1),nOps[i])
        testingList.append(eval(join(nSubList)))
        
        nSubList.clear()

    if True in testingList:
        return True
    else:
        return False
#Function to visualize when the numbers turn good or bad
startValue = 0
def plotCumulativeSum(xMin,xMax,addWhat,subtractWhat,logYesNo):
    global startValue 
    startValue = 0
    def func(x):
        
        result = testGoodBad(x)
        if result == True:
            addValue = addWhat
        else: 
            addValue = subtractWhat
        global startValue
        startValue = startValue + addValue
        return startValue
        
   
    # Ensure x is a list of integers
    x = list(range(xMin, xMax))

    # Apply func to each element in x
    y = [func(i-1) for i in x]  # Apply function element-wise

    # Plot the values
    plt.plot(x, y, linestyle = 'solid')
    plt.xlabel("x")
    if logYesNo == True:
        plt.xscale('log')
    plt.title("Good/Bad Cumulative Sum")
    plt.grid(True)
    plt.legend()
    plt.show()

plotCumulativeSum(100,6400,2,-1,False)