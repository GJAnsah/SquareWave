import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,linspace,pi
import ipywidgets as wg
from IPython.display import display

def Squareplot(c):
    x=np.linspace(-2*pi,2*pi,1000)      #giving an x range of -2pi to 2pi
    y=sin(x)
    a=3
    while a<2000:                     
        y=y+sin(a*x)/a                    
        a=a+2                            #this while loop is used to produce a square wave by adding odd harmonics from the 3rd to the 1999th.
    plt.plot(x,y)
    plt.show()
    
    
    y=sin(x)
    a=3
    while a<c:
        y=y+sin(a*x)/a
        a=a+2

    plt.plot(x,y)
    
c_slide=wg.IntSlider(value=3,min=3,max=2000,step=1)       #slider widget code to add slider
wg.interact(Squareplot, c=c_slide)                        #calling the function with the slider value
