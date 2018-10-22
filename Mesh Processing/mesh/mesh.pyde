# Christian Thai
# P5
# Sample code for starting the mesh processing project

rotate_flag = True    # automatic rotation of model?
time = 0   # keep track of passing time, for automatic rotation
import random

from cornerTable import *
from gtVector import *


geometryTable = []
vertexTable = []
cTable = None
colors = []

randFlag = False
vtxFlag = False
dualMesh = 0


# initalize stuff
def setup():
    size (600, 600, OPENGL)
    noStroke()

# dr the current mesh
def draw():
    global time
    global colors
    
    global randFlag
    global dualMesh
    global cTable
    global faceNumber
    background(0)    # clear screen to black

    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    scale (1, -1, 1)    # change to right-handed coordinate system
    
    # create an ambient light source
    ambientLight (102, 102, 102)
  
    # create two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    fill (50, 50, 200)            # set polygon color
    ambient (200, 200, 200)
    specular (0, 0, 0)            # no specular highlights
    shininess (1.0)
  
    rotate (time, 1.0, 0.0, 0.0)

    # THIS IS WHERE YOU SHOULD Dr THE MESH
    
    if cTable == None:
        beginShape()
        normal (0.0, 0.0, 1.0)
        vertex (-1.0, -1.0, 0.0)
        vertex ( 1.0, -1.0, 0.0)
        vertex ( 1.0,  1.0, 0.0)
        vertex (-1.0,  1.0, 0.0)
        endShape(CLOSE)
        
    else:
        c = cTable
        v = c.vTable
        g = c.gTable
        cornerCount = 0
        
        if dualMesh == 1:
            cTable = calcDM(cTable.gTable, cTable.vTable)
            faceNumber = len(cTable.vTable)/3
            colors = changeColors(faceNumber)
        for i in range(len(v)):
            
            if i % 3 == 0:
                
                if randFlag:
                    fill(colors[cornerCount][0], 
                         colors[cornerCount][1], 
                         colors[cornerCount][2])            
                else:
                    fill(200,200,200)
                beginShape()
            if vtxFlag:
                cNorm = calcNorm(i).gtScaler(-1).vector
                normal(cNorm[0], 
                       cNorm[1], 
                       cNorm[2])
            vertex(g[v[i]].x, 
                   g[v[i]].y, 
                   g[v[i]].z)    
            if i % 3 == 2:
                cornerCount=cornerCount+1
                endShape(CLOSE)
        dualMesh = 0
    popMatrix()
    
    if rotate_flag:
        time += 0.02

# process key presses
def keyPressed():
    global rotate_flag
    global randFlag
    global vtxFlag
    
    global dualMesh
    global colors
    
    if key == ' ':
        rotate_flag = not rotate_flag
    elif key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
    elif key == '5':
        read_mesh ('torus.ply')
    elif key == 'n':
        vtxFlag = not vtxFlag
    elif key == 'r':
        randFlag = True
        colors = changeColors(len(cTable.vTable)/3)
    elif key == 'w':
        randFlag = False
    elif key == 'd':
        dualMesh = dualMesh+1
    elif key == 'q':
        exit()

# read in a mesh file (THIS NEEDS TO BE MODIFIED !!!)
def read_mesh(filename):
    global geometryTable
    global vertexTable
    global cTable
    
    global randFlag
    
    global faceNumber
    global colors
    geometryTable = []
    vertexTable = []
    cTable = None
    
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex = ", x, y, z
        
        geometryTable.append(gtVertex(x, y, z))

    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if nverts != 3:
            print "error: this face is not a triangle"
            exit()    
        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        print "face =", index1, index2, index3
        
        vertexTable.append(index1)
        vertexTable.append(index2)
        vertexTable.append(index3)
        
    cTable=cornerTable(geometryTable,vertexTable)
    if randFlag == True:
        colors = changeColors(len(cTable.vTable)/3)

def changeColors(faceNumber):
    colorA = []
    for i in range(faceNumber):
        colorA.append((random.random() * 255, 
                           random.random() * 255, 
                           random.random() * 255))
    return colorA

def swing(i):
    global cTable
    
    c = cTable
    v = cTable.vTable
    
    return c.getN(c.getO(c.getN(i)))

def calcDM(g, v):
    global cTable
    topFace = []
    topCentroid = []
    centroidsList = []
    face = []    
    for vrtcs in range(0,len(v)):
        face.append(vrtcs)
        if vrtcs % 3==2:
            topFace.append(face)
            face = []
    tList = []
    for face in topFace:
        tList.append([v[face[0]], 
                      v[face[1]], 
                      v[face[2]]])
    vList = []
    for tri in tList:
        vList.append([g[tri[0]].vec, g[tri[1]].vec, g[tri[2]].vec])
        
    for vrtcs in vList:
        answer = vrtcs[0].gtAdd(vrtcs[1].gtAdd(vrtcs[2])).gtDiv(3)
        topCentroid.append(answer)
    
    averagefaces = []
    averageCentroids = []

    for vrtcs in range(0,len(g)):
        nowC = 0
        for c in range(len(v)):
            if v[c] == vrtcs:
                nowC = c
        nowCN = cTable.getN(nowC)
        nowCP = cTable.getP(nowC)    
        cornerConnects = []
        
        while [nowC, nowCN, nowCP] not in cornerConnects:
            cornerConnects.append([nowC, nowCN, nowCP])
            nowC = swing(nowC)
            nowCN = cTable.getN(nowC)
            nowCP = cTable.getP(nowC)    
        faceConnects = []
        for i in range(0, len(cornerConnects)):
            faceConnects.append([v[cornerConnects[i][0]], 
                                 v[cornerConnects[i][1]], 
                                 v[cornerConnects[i][2]]])
        centroidConnects = []
        for face in faceConnects:
            c = gtVector((0,0,0))
            for vrtcs in face:
                c = c.gtAdd(g[vrtcs].vec)
            c = c.gtDiv(3)
            centroidConnects.append(c)
        sum = gtVector((0,0,0))
        
        for c in centroidConnects:
            sum = sum.gtAdd(c)        
        average = sum.gtDiv(len(centroidConnects))
        averageCentroids.append(average)
        averagefaces.append((average,centroidConnects))
    newGeometryTble = topCentroid+averageCentroids
    convFaceAverage = []
    for average in averagefaces:
        avgCent = average[0]
        f = average[1]    
        temporary = []
        for i in range(len(f)):
            for j in range(len(newGeometryTble)):
                if round(f[i].vector[0], 3)==round(newGeometryTble[j].vector[0], 3) and round(f[i].vector[1], 3)==round(newGeometryTble[j].vector[1],3) and round(f[i].vector[2],3)==round(newGeometryTble[j].vector[2],3):
                    temporary.append(j)
        convFaceAverage.append((newGeometryTble.index(avgCent), temporary))
    
    lastVert = []
    for face in range(len(convFaceAverage)):
        now = convFaceAverage[face]
        for i in range (len(now[1])):
            if i+1 == len(now[1]):
                lastVert.append([now[1][i], 
                                      now[1][0], 
                                      now[0]])
            else:
                lastVert.append([now[1][i], 
                                      now[1][i+1], 
                                      now[0]])
    newVertTble = []
    for i in lastVert:
        newVertTble = newVertTble+i
    cGeometryTable = []
    for g in newGeometryTble:
        cGeometryTable.append(gtVertex(g.vector[0], 
                                       g.vector[1], 
                                       g.vector[2]))
    newGeometryTble = cGeometryTable
    yay = cornerTable(newGeometryTble,newVertTble)
    return yay

def calcNorm(i):
    
    global cTable
    
    c = cTable
    v = cTable.vTable
    g = cTable.gTable
    
    
    visitV = []
    aList = []

    vPoint = c.getN(i)
    while v[vPoint] not in visitV:
        visitV.append(v[vPoint])    
        if v[vPoint] != v[i]:
            aList.append(v[vPoint])
            vPoint = c.getN(swing(c.getP(vPoint)))
    rVert = [c.gTable[v[i]].vec]
    for vrtcs in aList:
        rVert.append(c.gTable[vrtcs].vec)

    vectorList = []
    for r in rVert:
        if r !=rVert[0]:
            vectorList.append(r.gtSub(rVert[0]))

    sum = gtVector((0,0,0))
    
    for vrtcs in range(0, len(vectorList)):
        
        if (vrtcs == len(vectorList)-1):        
            sum = sum.gtAdd(vectorList[vrtcs].gtCross(vectorList[0]))
            
        else:
            sum = sum.gtAdd(vectorList[vrtcs].gtCross(vectorList[vrtcs+1]))        
    return sum.gtNormalize()