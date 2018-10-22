# Optimus Prime bootleg version
# Author: Christian Thai

time = 0   # use time to move objects from one frame to the next
camZ = 300
camY = -200
camX = 0
rotate1 = 0
transform1 = 0
transform2 = 0
transform3 = 0
antRot = 0
antY = -10
antZ = 0
wheelY = 5
headY = -1
rotX = 0
def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    global camZ
    global camY
    global camX
    global rotate1
    global transform1
    global transform2
    global transform3
    global antRot
    global antY
    global antZ
    global wheelY
    global headY
    global rotX
    time += 0.01
    if (time < 10):
        camX = time*80
        camera (camX, -200, 300, time*100-400, 10, 0, 0,  1, 0)  # position the virtual camera
    elif (time < 12):
        camZ -= 0.5
        camY += 0.95
        camera(600,camY,camZ, 600,0,0,0,1,0)
    elif (time < 14):
        camera(600,-10,100,600,0,0,0,1,0)
    elif (time < (15.1 + PI/2)):
        camX = 600
        camZ = 100
        camera(600,-10,100,600,0,0,0,1,0)
    elif (time < 16.1 + PI/2):
        camX -= 1.5
        camZ -= 1
        camera(camX,-60,camZ,600,-30,0,0,1,0)
    else:
        camera(450,-60,0,600,-30,0,0,1,0)
        # camera(600,-10,100,600,0,0,0,1,0)
        

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a directional light source
    if (time < 20):
        ambientLight(50, 50, 50); 
        lightSpecular(255, 255, 255)
        directionalLight (100, 100, 100, -0.3, 0.5, -1)
    else:
        ambientLight(50, 50, 50); 
        lightSpecular(255, 255, 255)
        directionalLight (100, 100, 100, 0.5, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    
    pushMatrix() #road
    translate(0,15,0)
    for i in range(0,14):
        pushMatrix()
        translate(i*100-600,-1,0)
        fill(255,255,0)
        scale(50,1,30)
        box(1,1,1)
        popMatrix()
    fill(211,211,211)
    scale(1500,1,300)
    box(1,1,1)
    popMatrix()
    
    for i in range(0,10):
        pushMatrix()
        translate(-time*80,0,0)
        pushMatrix()
        if (i%2 == 0):
            translate(i*100,0,-80)
        else:
            translate(i*100,0,80)
        car()
        popMatrix()
        popMatrix()

    pushMatrix() #Start of the whole object
    if (time < 10): #Motion
        translate(time*100-400,0, 0)
    elif (time < 12):
        translate(600,0,0)
    elif (rotate1 > (-PI/2)) and (time > 12):
        rotate1 -= 0.01
        translate(600,rotate1*15,0)
        rotateZ(rotate1)
    elif (time > 22):
        rotX += 0.01
        translate(600,rotate1*15,0)
        rotateZ(-PI/2)
        rotateX(rotX)
    else: #pivot upwards
        translate(600,rotate1*15,0)
        rotateZ(-PI/2)

    pushMatrix() #Rotation body
    if (time < 14.5):
        translate(0,0,0)
        rotateZ(0)
    elif (time < (14.5 + PI/2) and (time > 14.5)):
        transform1 -= 0.01
        rotateZ(transform1)
    elif (time < (14.9 + PI/2)) and (time > (14.5 + PI/2)):
        transform2 += 0.5
        rotateZ(-PI/2)
        translate(0,transform2,0)
    elif ((time > (14.9 + PI/2)) and (time < (15.1 + PI/2))):
        transform3 -= 0.5
        rotateZ(-PI/2)
        translate(transform3,20,0)
    elif(time < 15.9 + PI):
        rotateZ(-PI/2)
        translate(-10,20,0)
    elif(time < 16.1 + PI):
        transform3 -= 0.5
        rotateZ(-PI/2)
        translate(transform3,20,0)
    else:
        rotateZ(-PI/2)
        translate(-20,20,0)
        

    fill(255,0,0) #Red Coloring for a segment
    pushMatrix() #Chest
    translate(20,0,0)
    box(30,10,20)
    
    pushMatrix() #Head
    fill(0,0,255)
    if (time < (15.9 + PI)):
        translate(0,-1,0)
    elif (time < (17 + PI)):
        headY += 0.1
        translate(0,headY,0)
    else:
        translate(0,10,0)
    box(10,10,10)
    fill(0,0,0)
    pushMatrix() #Eyes
    translate(5,2,-2)
    box(2,2,2)
    popMatrix()
    
    pushMatrix() 
    translate(5,2,2)
    box(2,2,2)
    popMatrix()   
    
    pushMatrix() #mouth
    fill(255,255,255)
    translate(5,-2,0)
    box(2,2,8)
    popMatrix()
    
    popMatrix()
    
    fill(255,0,0) #Red Coloring for a segment
    pushMatrix() #Chest 2
    translate(-5,-10,0)
    box(20,10,20)
    
    fill(0,0,255)
    pushMatrix() #Window 1
    translate(9.5,0,5)
    box(2,8,8)
    popMatrix()
    
    pushMatrix() #Window 2
    translate(9.5,0,-5)
    box(2,8,8)
    popMatrix()
    
    fill(211,211,211)
    pushMatrix() #Antenna 1
    if (time < 15.1 + PI/2):
        translate(8,-10,8)
        rotateX(PI/2)
    elif (time < 15.9 + PI/2):
        antY += .1
        translate(8,antY,8)
        rotateX(PI/2)
    elif(time < 15.9 + PI):
        antZ += (0.05)
        translate(8,10, 6 +antZ)
        rotateZ(PI/2)
    else:
        translate(8,10,15)
        rotateZ(PI/2)
    scale(1,1,5)
    cylinder()
    popMatrix()
    
    pushMatrix() #Antenna 2
    if (time < 15.1 + PI/2):
        translate(8,-10,-8)
        rotateX(PI/2)
    elif (time < 15.9 + PI/2):
        translate(8,antY,-8)
        rotateX(PI/2)
    elif(time < 15.9 + PI):
        translate(8,10, -6 - antZ)
        rotateZ(-PI/2)
    else:
        translate(8,10,-15)
        rotateZ(-PI/2)
    scale(1,1,5)
    cylinder()
    popMatrix()
    
    popMatrix() #close chest 2
    fill(192,192,192)
    pushMatrix() #Grill
    translate(15,0,0)
    box(2,8,18)
    popMatrix()
    
    fill(0,0,0)
    pushMatrix()#Front wheel 1
    if (time < 15.9+ PI/2):
        translate(0,5,8)
    elif (time < 15.9 + PI):
        wheelY -= (0.05)
        translate(0,wheelY,8)
    else:
        translate(0,0,8)
    scale(5,5,1)
    
    cylinder()
    popMatrix()
    
    pushMatrix()#Front wheel 2
    if (time < 15.9+ PI/2):
        translate(0,5,-8)
    elif (time < 15.9 + PI):
        translate(0,wheelY,-8)
    else:
        translate(0,0,-8)
    scale(5,5,1)
    cylinder()
    popMatrix()
    
    popMatrix() #close rotation body
    popMatrix() #close head
    
    pushMatrix() #Legs
    translate(20,0,0)
    fill(0,0,255)
    pushMatrix() #Legs
    translate(-35,0,5)
    box(40,10,10)
    popMatrix()
    
    pushMatrix() #legs 2
    translate(-35,0,-5)
    box(40,10,10)
    popMatrix()
    
    fill(0,0,0)
    pushMatrix() #foot 1
    translate(-52.5,-9, 6)
    box(5, 8 ,8)
    popMatrix()
    
    pushMatrix() #foot 1
    translate(-52.5,-9,-6)
    box(5, 8 ,8)
    popMatrix()
    

    
    pushMatrix()#Back Wheels 1
    translate(-25,5,8)
    scale(5,5,1)
    pushMatrix()
    translate(-3,0,0)
    cylinder()
    popMatrix()
    cylinder()
    popMatrix()
    
    pushMatrix()#Back Wheels 2
    translate(-25,5,-8)
    scale(5,5,1)
    pushMatrix()
    translate(-3,0,0)
    cylinder()
    popMatrix()
    cylinder()
    popMatrix()
    popMatrix() #close Legs
    popMatrix() #End of whole object


def car():
    pushMatrix()
    fill(255,255,0)
    box(30,10,20)
    
    pushMatrix()
    fill(0,0,0)
    translate(0,-10,0)
    box(15,10,15)
    popMatrix()
    
    pushMatrix()
    translate(8,5,8)
    scale(4,4,1)
    cylinder()
    pushMatrix()
    translate(-4,0,0)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(0,0,-16)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(-4,0,-16)
    cylinder()
    popMatrix()
    
    popMatrix()
    
    popMatrix()
    
    
# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2