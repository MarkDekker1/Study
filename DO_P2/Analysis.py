import numpy as np
import matplotlib
import matplotlib.pyplot as plt

np.seterr(over='raise')

mx=50
mt=1000
my=10
Deltax=1./mx
Deltat=1./mt
Deltay=1./my
tmax=10.
L=1.
Ly=1.

r=0.1
Lambda=10000

Cw0=1./(Deltat*Deltax**2.)-1./(4.*Deltax)+r/(2.*Deltax**2.)
Cc0=-(2./(Deltat*Deltax**2.)+(Lambda+1)/Deltat+r/(Deltax**2.)+r/2.)
Ce0=1./(Deltat*Deltax**2.)+1./(4.*Deltax)+r/(2.*Deltax**2.)

def h(phimin1,phi1,phiplus1):
    return ((phiplus1-2.*phi1+phimin1)/(Deltat*Deltax**2.)+(Lambda+1.)*phi1/Deltat
    -(phiplus1-phimin1)/(4.*Deltax)-r*((phiplus1-2.*phi1+phimin1)/(2.*Deltax**2.)-phi1/2.)+1.)

a=Cw0
a0=0.
b=Cc0
c=Ce0
c1=0.

#First create a vector at time 1
dvt=[]
bvt=[]
psiv=np.zeros(mx)
psivt=np.zeros(shape=(mt,len(psiv)))
dv=np.zeros(mx)
bv=np.zeros(mx)+Cc0
bv[0]=Cc0
psivt=np.zeros(shape=(mt,len(psiv)))
psipast=psiv

for i in range(0,mt):
    if i>0:
        psipast=psivt[i-1]
        
    
    for x in range(0,1):
        dv[x]=h(0,psipast[x],psipast[x+1])    
        m=a0/bv[x]
        bv[x]=bv[x]-m*c
        dv[x]=dv[x]
    
    for x in range(1,int(mx-1)):
        dv[x]=h(psipast[x-1],psipast[x],psipast[x+1])    
        m=a/bv[x-1]
        bv[x]=bv[x]-m*c
        dv[x]=dv[x]-m*dv[x-1]
    
    for x in range(int(mx-1),int(mx)):
        dv[x]=h(psipast[x-1],psipast[x],0.)
        c1=0.    
        m=a/bv[x-1]
        bv[x]=bv[x]-m*c1
        dv[x]=dv[x]-m*dv[x-1]
        
    #Backwise
    psiv[int(mx-1)]=dv[int(mx-1)]/bv[int(mx-1)]
    for x in np.linspace(0,int(mx-2),int(mx-1))[::-1]:
        psiv[x]=(dv[x]-c*psipast[x+1])/bv[x]
    psivt[i]=psiv
#%%
plt.plot(psiv)
plt.show()
plt.contourf(psivt)
plt.colorbar()
plt.show()

#%%#Choose a time
Time=5
totalpsivec=np.zeros(shape=(my,mx))
Xdist=np.linspace(0,1,mx)
Ydist=np.linspace(0,1,my)
for i in range(0,my):
    for j in range(0,mx):
        totalpsivec[i][j]=psivt[Time][j]*np.sin(i)
        
plt.contourf(Xdist,Ydist,totalpsivec,25)
plt.xlabel('zonal distance')
plt.ylabel('meridional distance')
plt.colorbar()
plt.show()