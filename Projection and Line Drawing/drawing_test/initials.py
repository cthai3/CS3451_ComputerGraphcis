# In the routine below, you should draw your initials in perspective

from matlib import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective (30, -30, 30)
    
    gtPushMatrix()
    gtTranslate(0,0,-4)

    #C
    gtVertex(-0.6,0.4,-1.5)
    gtVertex(-0.6,-0.4,1.5)
    
    gtVertex(-0.6,0.4,-1.5)
    gtVertex(0.2,0.4,-1.5)
    
    gtVertex(-0.6,-0.4,1.5)
    gtVertex(0.2,-0.4,1.5)
    
    #T
    gtVertex(0.6,0,-1.5)
    gtVertex(0.6,-0.8,1.5)
    
    gtVertex(0.2,0,-1.5)
    gtVertex(1.0, 0, -1.5)
    
    gtPopMatrix()