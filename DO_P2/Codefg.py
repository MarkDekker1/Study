# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:10:54 2016

@author: Swinda
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

np.seterr(over='raise')

mx=100
mt=500
dx=1./mx
dt=10000
tmax=500000.
L=1.

r=0.1
Lambda=0.


Cw0=1./(dt*dx**2)-1./(4.*dx)+r/(2.*dx**2)
Cc0=-(2./(dt*dx**2)+(Lambda+1)/dt+r/(dx**2)+r/2.)
Ce0=1./(dt*dx**2)+1./(4.*dx)+r/(2.*dx**2)

#def hf(phim1,phi1,phip1):
#    return ((phip1-2.*phi1+phim1)/(dt*dx**2)+(Lambda+1)*phi1/dt-(phip1-phim1)/(4.*dx)-r*((phip1-2*phi1+phim1)/(2*dx**2)-phi1/2.)+1.)

def hf(phim1,phi1,phip1):
    return (phip1-2*phi1+phim1)/(dt*dx**2)+(Lambda+1)*phi1/dt-(phip1-phim1)/(4*dx)-r*((phip1-2*phi1+phim1)/(2*dx**2)-phi1/2.)+1.
    

n=mx
tt=int(tmax/dt)
#b0=Cc0*np.ones(n)
h=np.zeros(n)
phin=np.zeros(n)
phip=np.zeros(shape=(tt,n))

#for t in range(0,tt):
#    b=b0
#    phi=phin
#    h[0]=hf(0.,phi[0],phi[1])
#    for i in range(1,n-1):
#        h[i]=hf(phi[i-1],phi[i],phi[i+1])
    #h[n-1]=hf(phi[n-2],phi[n-1],0.)
    
#    h0=h
#    for k in range(1,n-1):
#        m = Cw0/b[k-1]
#        b[k] = Cc0-m*Ce0
#        h[k] = h0[k]-m*h0[k-1]
    
#    phin[n-1] = h[n-1]/b[n-1]
#    for j in range(n-2,0,-1):
#        phin[j]=(h[j]-Ce0*phin[j+1])/b[j]
        
#    phip[t]=phin
    
b=np.zeros(n)
phi=np.zeros(n)


#for t in range(0,int(tmax*mt)):
for t in range(0,tt):
    h[0]=hf(0.,phi[0],phi[1])
    for k in range(1,n-1):
        h[k]=hf(phi[k-1],phi[k],phi[k+1])
    h[n-1]=hf(phi[n-2],phi[n-1],0.)
    
    for i in range(0,n):
        b[i]=Cc0
    for k in range(1,n):
        m=Cw0/b[k-1]
        b[k]=b[k]-m*Ce0
        h[k]=h[k]-m*h[k-1]
        
    phin[n-1]=h[n-1]/b[n-1]
    for k in range(n-2,0,-1):
        phin[k]=(h[k]-Ce0*phin[k+1])/b[k]
    phi=phin
    
    phip[t]=phi

print phin

    
b=np.zeros(n)
phi=np.zeros(n)


# Data Placeholders
yp1=np.zeros(0)

xvec,yvec=np.meshgrid(xvec,yvec)

#Radiation plot
LIJN1, = ax01.plot(t,yp1,'b-', label="QS")

#Timeloop
def plotter(vec):
    return np.array(np.transpose([vec[0:3],vec[3:6],vec[6:9]]))
    
def init():
    imobj.set_data(Ta)
    time_text.set_text('time = 0.0')

    return imobj , time_text
    
def animate(self):
    global data
    global LIJN1
    global t
    global x
    global yp1
    global qk
    
    
    #for t in range(0,int(tmax*mt)):
    for t in range(0,tt):
        h[0]=hf(0.,phi[0],phi[1])
        for k in range(1,n-1):
            h[k]=hf(phi[k-1],phi[k],phi[k+1])
        h[n-1]=hf(phi[n-2],phi[n-1],0.)
        
        for i in range(0,n):
            b[i]=Cc0
        for k in range(1,n):
            m=Cw0/b[k-1]
            b[k]=b[k]-m*Ce0
            h[k]=h[k]-m*h[k-1]
            
        phin[n-1]=h[n-1]/b[n-1]
        for k in range(n-2,0,-1):
            phin[k]=(h[k]-Ce0*phin[k+1])/b[k]
        phi=phin
        
        phip[t]=phi    
    
    
    yp1=np.append(yp1,np.mean(QS))
    t=np.append(t,x)

    x += 1.0    
    
    LIJN1.set_data(t,yp1)
    
    time_text.set_text('time = %.1f' % self )
    new=plotter(Ts)
    imobj.set_data(new)
       
    imobj.set_zorder(0)
    Quivers.set_UVC(plotter(U),plotter(V))
    
    ax1=plt.axhline(xmin=0,xmax=1,y=0,linewidth=3,color='k')
    
    return imobj,time_text,ax1,LIJN1
xax=np.linspace(0.,1.,mx)

X,Y=np.meshgrid([0,1,2],[2,1,0])

l, r, b, top = plt.axis()
dx, dy = r - l, top - b
plt.axis([l - 0.05*dx, r + 0.05*dx, b - 0.05*dy, top + 0.05*dy])

line_simu, = plt.plot([], [],"r--", lw=2, markersize=4 , label = "Some curve" ,  zorder= 1 )
time_text = plt.text(0.1, 0.1, '', zorder=10)

anim = animation.FuncAnimation(fig, animate,  frames=range(1000), interval=200,blit=True,repeat=False)
