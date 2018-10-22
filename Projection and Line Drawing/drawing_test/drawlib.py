# Drawing Routines, like OpenGL

from matlib import *

isOrth = True

leftV = 0
rightV = 0
botV = 0
topV = 0
nearV = 0
farV = 0
fovV = 0

firstVertex = False
V1 = (0, 0, 0)
vertexP = []
# shape_on = False

def gtOrtho(left, right, bottom, top, near, far):
    global isOrth
    global leftV
    global rightV
    global botV
    global topV
    global nearV
    global farV
    
    isOrth = True
    leftV = left
    rightV = right
    botV = bottom
    topV = top
    nearV = near
    farV = far

def gtPerspective(fov, near, far):
    global isOrth
    isOrth = False
    
    global fovV 
    fovV = fov

def gtBeginShape():
    # global shape_on
    # if not shape_on:
    #     shape_on = True
    # else:
    #     print "Shape Cannot Begin"
    pass

def gtEndShape():
    # global shape_on
    # if shape_on:
    #     shape_on = Flase
    # else:
    #     print "Shape Cannot End"
    pass

def gtVertex(x, y, z):
    global firstVertex
    global vertexP
    if firstVertex == False:
        firstVertex = True
        vertexP = [[x],[y],[z],[1]]
    else:
        sV = vertexP
        eV = [[x],[y],[z],[1]]
        
        sV = gtMultiply(stack[len(stack)-1].data, sV)
        eV = gtMultiply(stack[len(stack)-1].data, eV)
    
        if isOrth:
            sVX = orthoX(sV[0][0], leftV, rightV)
            sVY = orthoY(sV[1][0], topV, botV)
            eVX = orthoX(eV[0][0], leftV, rightV)
            eVY = orthoY(eV[1][0], topV, botV)
        else:
            sVX = povX(sV[0][0], fovV, sV[2][0])
            sVY = povY(sV[1][0], fovV, sV[2][0])
            eVX = povX(eV[0][0], fovV, eV[2][0])            
            eVY = povY(eV[1][0], fovV, eV[2][0])
            
        line(sVX, sVY, eVX, eVY)
        global firstVertex
        global vertexP
        
        firstVertex = False
        vertexP = []
        
def orthoX(x, left, right):
    newX = (width / (right - left)) * (x - left)
    return float(newX)

def orthoY(y, top, bottom):
    newY = (height / (bottom - top)) * (y - top)
    return float(newY)

def povX(x, fov, z):
    newX = x / abs(z)
    k = tan((fov*PI/180.0)/2.0)
    newerX = (newX + k) * (width / (2*k))
    return float(newerX)

def povY(y, fov, z):
    newY = y / abs(z) * -1
    if z == 0:
        z = 1
    k = tan((fov*PI/180.0)/2)
    newerY = (newY + k)*(width / (2*k))
    return float(newerY)
    