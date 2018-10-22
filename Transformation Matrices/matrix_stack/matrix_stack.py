# Matrix Stack Library
# Version 1.0 by Christian Thai
# CS3451-A Project 1A 

# you should modify the routines below to complete the assignment
stack = []

def gtInitialize():
    global stack
    stack = []
    m = Matrix()
    stack.append(m)

def gtPushMatrix():
    global stack
    toCopy = stack[len(stack)-1] #Gets top of the stack
    toPush = Matrix()
    clone = toCopy.data[:]
    toPush.data = clone #copies the matrix
    stack.append(toPush)

def gtPopMatrix():
    global stack
    if (len(stack) <= 1):
        print("Matrix Stack only has one matrix, cannot pop Matrix!")
    stack.pop()

def gtTranslate(x, y, z):
    global stack
    tMatrix = Matrix()
    tData = tMatrix.data
    tData[0][3] = x
    tData[1][3] = y
    tData[2][3] = z
    tMatrix.data = tData
    stack[len(stack)-1].data = stack[len(stack)-1].multiply(tMatrix)

def gtScale(x, y, z):
    global stack
    tMatrix = Matrix()
    tData = tMatrix.data
    tData[0][0] = x
    tData[1][1] = y
    tData[2][2] = z
    tMatrix.data = tData
    stack[len(stack)-1].data = stack[len(stack)-1].multiply(tMatrix)

def gtRotateX(theta):
    global stack
    rads = radians(theta)
    tMatrix = Matrix()
    tData = tMatrix.data
    tData[1][1] = cos(rads)
    tData[1][2] = -sin(rads)
    tData[2][1] = sin(rads)
    tData[2][2] = cos(rads)
    tMatrix.data = tData
    stack[len(stack)-1].data = stack[len(stack)-1].multiply(tMatrix)

def gtRotateY(theta):
    global stack
    rads = radians(theta)
    tMatrix = Matrix()
    tData = tMatrix.data
    tData[0][0] = cos(rads)
    tData[2][0] = -sin(rads)
    tData[0][2] = sin(rads)
    tData[2][2] = cos(rads)
    tMatrix.data = tData
    stack[len(stack)-1].data = stack[len(stack)-1].multiply(tMatrix)

def gtRotateZ(theta):
    global stack
    rads = radians(theta)
    tMatrix = Matrix()
    tData = tMatrix.data
    tData[0][0] = cos(rads)
    tData[0][1] = -sin(rads)
    tData[1][0] = sin(rads)
    tData[1][1] = cos(rads)
    tMatrix.data = tData
    stack[len(stack)-1].data = stack[len(stack)-1].multiply(tMatrix)

def gtGetMatrix():
    pass

def print_ctm():
    global stack
    ctm = stack[len(stack)-1]
    for i in range(4):
        p = "["
        row = ctm.data[i]
        for j in range(4):
            num = row[j]
            if (j < 3): #if it's not the end of the row
                p += (str(num) + ", ") #Add the next number to the print statement
            else:
                p += (str(num) + "]")
        print(p)
    print(" ")
    
#Helper Class to represent a Matrix
class Matrix():
    #Initializes a Matrix with 4x4 identity matrix as the data.
    def __init__(self):
        self.data = []
        self.data.append([1,0,0,0])
        self.data.append([0,1,0,0])
        self.data.append([0,0,1,0])
        self.data.append([0,0,0,1])
    
    #Method for Matrix Multiplication
    #Returns a 2D list representing Matrix data
    def multiply(self, m):
        a = self.data
        b = m.data
        result = [[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
        for x in range(4):
            row = a[x]
            for y in range(4):
                dp = 0
                for z in range(4):
                    temp = b[z]
                    rowNum = row[z]
                    colNum = temp[y]
                    dp += (rowNum*colNum)
                result[x][y] = dp
        return result    