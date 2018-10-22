class Vertex:
    
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

class Fov:
    
    def __init__(self, angle):
         self.angle = float(angle)
    
    def convertToRadians(self):
        return float(self.angle * PI / 180.0)
        
class Background:
    
    def __init__(self, r, g, b):
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)
    
class Light:
    
    def __init__(self, x, y, z, r, g, b):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)

class Surface:
    
    def __init__(self, Cdr, Cdg, Cdb, Car, Cag, Cab, Csr, Csg, Csb, P, Krefl):
        self.Cdr = float(Cdr)
        self.Cdg = float(Cdg)
        self.Cdb = float(Cdb)
        self.Car = Car
        self.Cag = Cag
        self.Csr = Csr
        self.Csg = Csg
        self.Csb = Csb
        self.P = P
        self.Krefl = Krefl

class Sphere:
    
    def __init__(self, radius, x, y, z):
        self.radius = radius
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    #intersection of eyeray
    def getIntersection(self, ray):
        rayDx = ray.getDx()
        rayDy = ray.getDy()
        rayDz = ray.getDz()    
        v1 = ray.vertex1
        a = rayDx**2 + rayDy**2 + rayDz**2
        b = (((v1.x * rayDx) - (self.x * rayDx)) + ((v1.y * rayDy) - (self.y * rayDy)) + ((v1.z * rayDz) - self.z * rayDz)) * 2
        c = (v1.x - self.x)**2 + (v1.y - self.y)**2 + (v1.z - self.z)**2 - (self.radius)**2
        disc = (b * b) - (4 * a * c)
        if disc > 0:
            t1 = (-b - sqrt(disc))/(2 * a)
            t2 = (-b + sqrt(disc))/(2 * a)
            t = min(t1,t2)
            if t < 0:
                return None    
            xt = v1.x + t * rayDx
            yt = v1.y + t * rayDy
            zt = v1.z + t * rayDz
            return Vertex(xt, yt, zt)    
        elif disc == 0:
            t = (-b - sqrt(disc)) / (2 * a)
            if t < 0:
                return None
            
            xt = v1.x + t * rayDx
            yt = v1.y + t * rayDy
            zt = v1.z + t * rayDz
            return Vertex(xt, yt, zt)    
        else:
            return None
        
class Ray:
    
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        
    def getDx(self):
        magnitude = sqrt((self.vertex2.x - self.vertex1.x)**2 +
                         (self.vertex2.y - self.vertex1.y)**2 + 
                         (self.vertex2.z - self.vertex1.x)**2)
        return float(self.vertex2.x - self.vertex1.x)
    
    def getDy(self):
        magnitude = sqrt((self.vertex2.x - self.vertex1.x)**2 +
                         (self.vertex2.y - self.vertex1.y)**2 + 
                         (self.vertex2.z - self.vertex1.x)**2)
        return float(self.vertex2.y - self.vertex1.y)
    
    def getDz(self):
        magnitude = sqrt((self.vertex2.x - self.vertex1.x)**2 +
                         (self.vertex2.y - self.vertex1.y)**2 + 
                         (self.vertex2.z - self.vertex1.x)**2)
        return float(self.vertex2.z - self.vertex1.z)