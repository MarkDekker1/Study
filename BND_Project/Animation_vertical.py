import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

Lat=Lat
Lvls=Levels[1:14]
x,y=meshgrid(Lat,Lvls)

fig = plt.figure()
ax=plt.axes(xlim=(0,len(Lat)),ylim=(0,len(Lvls)))
plt.xlabel('x')
plt.ylabel('y')

z=Fvec[0]
cont = plt.contourf(x,y,z,25)

def animate(i):
    z= Fvec[i]
    if (i==0):
        plt.title (r't=%1.2e'% i)
    else:
        plt.title(r't=%i'%i)
    
    cont.set_data(x,y,z)
    return cont
    
anim = animation.FuncAnimation(fig,animate,frames=10)