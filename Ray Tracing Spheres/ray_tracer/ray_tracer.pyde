# This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.
# Author: Christian Thai
from scenes import *

fov = 0
bg = Background(0, 0, 0)
sph = Sphere(1, 0, 0, 0)
l = Light(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
s = Surface(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

sphList = []
lList = []
sList = []

def setup():
    size(500, 500) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    if key == '1':
        reset()
        interpreter("i1.cli")
    elif key == '2':
        reset()
        interpreter("i2.cli")
    elif key == '3':
        reset()
        interpreter("i3.cli")
    elif key == '4':
        reset()
        interpreter("i4.cli")
    elif key == '5':
        reset()
        interpreter("i5.cli")
    elif key == '6':
        reset()
        interpreter("i6.cli")
    elif key == '7':
        reset()
        interpreter("i7.cli")
    elif key == '8':
        reset()
        interpreter("i8.cli")
    elif key == '9':
        reset()
        interpreter("i9.cli")

def interpreter(fname):
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            # call your sphere creation routine here
            # for example: create_sphere(radius,x,y,z)
            global sph
            sph = Sphere(radius, x, y, z)
            global sphList
            sphList.append(sph)
            
        elif words[0] == 'fov':
            global fov
            fov = Fov(words[1])
        elif words[0] == 'background':
            global bg
            bg = Background(words[1], words[2], words[3])
        elif words[0] == 'light':
            lightX = words[1]
            lightY = words[2]
            lightZ = words[3]
            lightR = words[4]
            lightG = words[5]
            lightB = words[6]
            global l
            l = Light(lightX, lightY, lightZ, lightR, lightG, lightB)
            global lList
            lList.append(l)
        elif words[0] == 'surface':
            global s
            s = Surface(words[1], words[2], words[3], words[4], words[5], words[6], 
                        words[7], words[8], words[9], words[10], words[11])
            global sList
            sList.append(s)
        elif words[0] == 'begin':
            pass
        elif words[0] == 'vertex':
            pass
        elif words[0] == 'end':
            pass
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    for j in range(height):
        for i in range(width):
            #screen-coordinate-to-3D-formula
            z = -1
            zPrime = z
            fovRadians = fov.convertToRadians()
            
            k = tan(fovRadians/2.0)        
            x = i / abs(z)
            xPrime = (x-(width/2.0)) * ((2.0*k)/width)
            y = (height-j)/abs(z)
            yPrime = (y-(height / 2.0)) * ((2.0*k)/height)
            



            closestObj = None
            surfaceCol = None
            intersection = None
            for n in range(len(sphList)): 
                object = sphList[n]
                objectSurface = sList[n]
                
                ray = Ray(Vertex(0,0,0), Vertex(xPrime, yPrime, zPrime))
                intersectionP = object.getIntersection(ray)
                if not intersectionP == None and not intersection == None: 
                    oldDistribution = dist(0, 0, 0, intersection.x, intersection.y, intersection.z)
                    newDistribution = dist(0, 0, 0, intersectionP.x, intersectionP.y, intersectionP.z)
                if not intersectionP == None and (intersection == None or (oldDistribution > newDistribution)):
                    intersection = intersectionP
                    closestObj = object
                    surfaceCol = objectSurface    
            if not closestObj == None: 
                colR = 0.0
                colG = 0.0
                colB = 0.0
                sphereCenter = PVector(closestObj.x, closestObj.y, closestObj.z)
                intersect = PVector(intersection.x, intersection.y, intersection.z)
                surfaceNormal = (intersect - sphereCenter).normalize()    
                for lightcol in lList:
                    lightPosition = PVector(float(lightcol.x), float(lightcol.y), float(lightcol.z))
                    lightNormal = (lightPosition - intersect).normalize() 
                    
                 #color equation   
                    colR += float(lightcol.r) * float(surfaceCol.Cdr) * max(0, surfaceNormal.dot(lightNormal))
                    colG += float(lightcol.g) * float(surfaceCol.Cdg) * max(0, surfaceNormal.dot(lightNormal))
                    colB += float(lightcol.b) * float(surfaceCol.Cdb) * max(0, surfaceNormal.dot(lightNormal))
                if colR > 1.0: 
                    colR = 1.0
                if colG > 1.0: 
                    colG = 1.0
                if colB > 1.0:
                    colB = 1.0
                pixel_color = color(colR, colG, colB)  # you should calculate the correct pixel color here
                set (i, j, pixel_color)         # fill the pixel with the calculated color
            else: 
                pixel_color = color(float(bg.r), float(bg.g), float(bg.b))
                set (i, j, pixel_color)    
# should remain empty for this assignment
def draw():
    pass
    
def reset():
    global bg
    bg = Background(0,0,0)
    
    global lList
    lList = []
    
    global sList
    sList = []
    
    global sphList
    sphList = []