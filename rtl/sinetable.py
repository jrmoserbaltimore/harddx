from numpy import sin, log2
from math import tau

class SineTable:
    def __init__(self):
        pass

class DX7SineTable(SineTable):
    def __init__(self):
        self.logSin = []
        for i in range(0,1024):
            w = (i+0.5)/1024
            y = numpy.log2(numpy.sin(w*tau/4))
            
        print("{}π/2 {} {}".format(w,y,int(y*1024+0.5002)))