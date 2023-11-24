from numpy import sin, log2
from math import tau

# This is rough code to illustrate how to eventually calculate sine
# and logsine in various ways.  The DX7 uses a 1024-entry quarter-sine
# table; we can also use a sixth-order polynomial cosine approximation,
# which we can embed in the hardware as a polynomial function instead
# of a table.  Which to use depends on the goal.
#
# One approach is to internally generate cos(w) by generating
# cosPolynomial(w/tau) for phase normalized to [0,1).  That would not
# be a numerically accurate representation of the DX7; it would use
# 1 multiply and 3 multiply-add circuits in series.

class SineTable:
    def __init__(self):
        pass

class DX7SineTable(SineTable):
    def __init__(self):
        self.logSin = []
        for i in range(0,1024):
            w = (i+0.5)/1024
            y = numpy.log2(numpy.sin(w*tau/4))
            self.logSin.append(int(y*1024+0.5002))
            
class PolynomialCosineTable(SineTable):
    # https://gist.github.com/publik-void/067f7f2fef32dbe5c27d6e215f824c91#cos-rel-error-minimized-degree-6
    def __init__(self):
        self.sinTable = []
        for i in range(0,1024):
            # minimum relative error for x=x, not normalized to tau.
            x2=i**2
            self.sinTable.append(0.999970210689953068626323587055728078
                                 + x2*(-0.499782706704688809140466617726333455
                                       + x2*(0.0413661149638482252569383872576459943
                                             - 0.0012412397582398600702129604944720102*x2)))
WL-sty