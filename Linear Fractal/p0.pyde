def setup():
    size(600, 600)
    
def draw():
    background(255, 255, 255)
    stringx = str(convertCoor(mouseX))
    stringy = str(convertCoor(mouseY))
    fill(50)
    text("V= (" + stringx + "," + stringy + ") :", 10, 10, 120, 20)
    for i in range(6):
        #horizontal
        stroke(0)
        line(0, (i*100), width, (i*100))
        #vertical
        line((i*100), 0, (i*100), height)
    noStroke()
    x = convertCoor(mouseX)
    y = convertCoor(mouseY)
    pos = Complex(x, y)
    n = 0
    zero = Complex(0, 0)
    zero.complexDraw()
    createFractal(pos, zero ,n)
    
def gridLines():
    for i in range(6):
        #horizontal
        fill(0)
        line(0, (i*100), width, (i*100))
        #vertical
        line((i*100), 0, (i*100), height)
    
def convertCoor(x):
    x = x - 300
    x = float(x)
    x = x / 100
    return x;

def revertCoor(x):
    x = x * 100
    x = x + 300
    return x;
    
def createFractal(pos, c, n):
    if (n == 10):
        return;
    d = c.complexAdd(pos.complexPow(n))
    d.complexDraw()
    createFractal(pos, d, n+1)
    e = c.complexSub(pos.complexPow(n))
    e.complexDraw()
    createFractal(pos, e, n+1)
    
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def complexAdd(self, c):
        real = self.a + c.a
        img = self.b + c.b
        d = Complex(real, img)
        return d;
        
    def complexSub(self, c):
        real = self.a - c.a
        img = self.b - c.b
        d = Complex(real, img)
        return d;
    
    def complexMult(self, c):
        real = ((self.a*c.a) - (self.b*c.b))
        img = ((self.a*c.b) + (self.b*c.a))
        d = Complex(real, img)
        return d;
    
    def complexPow(self, n):
        if (n == 0):
            d = Complex(1, 0)
            return d
        d = self
        for i in range(n-1):
            d = d.complexMult(self)
        return d;
    
    def complexDraw(self):
        x = self.a
        x = revertCoor(x)
        y = self.b
        y = revertCoor(y)
        bright = 0
            if (mouseY <= 200):
                bright = 255
            elif (mouseY <= 400):
                bright = 170
            else:
                bright = 85
        r = 0
        g = 0
        boo = 0
        if (mouseX <= 200):
            r = (1*bright)
        elif (mouseX <= 400):
            g = (1*bright)
        else:
            boo = (1*bright)
        
        fill(r, g, boo)
        ellipse(x, y, 10, 10)
    