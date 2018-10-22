import math

class gtVector:
    
    def __init__(self, vector):
        self.vector = vector
    def gtAdd(self, v):
        return gtVector([self.vector[i] + v.vector[i] for i in range(len(self.vector)) ])
    def gtSub(self, v):
        return gtVector([self.vector[i] - v.vector[i] for i in range(len(self.vector)) ])
    def gtScaler(self,scaler):
        return gtVector([self.vector[i] * scaler for i in range(len(self.vector)) ])
    def gtDiv(self, divide):
        return gtVector([self.vector[i] / divide for i in range(len(self.vector)) ])
    def gtDot(self, vector2):
        return sum([i * j for (i, j) in zip(self.vector, vector2.vector)])
    def gtMagnitude(self):
        return math.sqrt(sum(self.vector[i] * self.vector[i] for i in range(len(self.vector))))
    def gtNormalize(self):
        magn = self.gtMagnitude()
        return gtVector([self.vector[i] / magn for i in range(len(self.vector))])
    def gtCross(self, vector2):
        a = self.vector
        b = vector2.vector
        c = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
        return gtVector(c)
    def __repr__(self):
        return str(self.vector)
    
    