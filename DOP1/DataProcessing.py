#Packages
from netCDF4 import Dataset
from pylab import * 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import scipy

#Constantem
Cd=0.0015
rhoa=1.225
rhow=1000.
beta0=2*10**(-11)

#Calculate Stresses
Ustress=rhoa*Cd*U**2*U/abs(U)
Vstress=rhoa*Cd*V**2*V/abs(V)

#Defining function for length between two meridionals
def xlen(latitude):
    return abs(6400000*2*np.pi/360*sin((latitude-90)/360.*2.*np.pi))

#Defining right boundary of the North Atlantic for discrete integration
Bvec=[]
for i in range(0,181):
    Boundary=0.
    k=150
    if i<30:
	 k=180
    while Dtot[i][k]>0 and k<359:
        Boundary=k
        k=k+1      
    Bvec.append(Boundary)
Bvec[51]=170.
Bvec[54]=172.

#Calculate Curl of stress and stream function
Curlstressvec=[]
Stream=np.zeros(shape=(181,360))
ylength=1./360.*2.*np.pi*6400000.

for i in range(0,181):
    phi=i-90.
    xlength=xlen(phi)
    Curlstressvec.append(gradient(Vstress[i,:])/(xlength)-np.transpose(gradient(np.transpose(Ustress)[:,i]))/ylength)
    for j in range(0,360):
	a=Curlstressvec[i]
	Stream[i,j]=sum(a[j:Bvec[i]])*(Bvec[i]-j)*xlength
        
Stream=Stream/(beta0*rhow*Dtot)

#Calculate Meridional and Zonal velocity
VelocityV=np.array(Curlstressvec)/(beta0*rhow*Dtot)
VelocityU=[]

for i in range(0,360):
	 VelocityU.append(-gradient(np.transpose(Stream)[i])/ylength)
	
VelocityU=np.transpose(VelocityU)/10

VelocityT=np.sqrt(VelocityU**2+VelocityV**2)

#%%
for i in range(0,len(VelocityV)):
	for j in range(0,len(VelocityV[1])):
		if abs(VelocityV[i,j])>5:
			VelocityV[i,j]=0
		if abs(VelocityU[i,j])>5:
			VelocityU[i,j]=0
		if j>210 or j<90 or i>80 or j<20:
			VelocityV[i,j]=0
			VelocityU[i,j]=0
			
