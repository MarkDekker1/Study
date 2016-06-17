#Modules
import numpy as np
import matplotlib.pyplot as plt

#Constants
U=10.
rho0=1000.
alpha=1.
f0=1e-4
g=9.81

#Functions
def stream(y,z):
	return -U*y*(alpha*z+1.)
	
def u(y,z):
	return U*(alpha*z+1.)
	
def rho(y,z):
	return -f0*rho0*(-U*y*alpha)/g+rho0
	
#Fields
Zvec=np.linspace(-1,0,100,endpoint=True)
Yvec=np.linspace(0,1,100,endpoint=True)
Uvec=np.zeros(shape=(100,100))
Rvec=np.zeros(shape=(100,100))
Svec=np.zeros(shape=(100,100))

for i in range(0,100):
	ycoord = np.linspace(0,1,100,endpoint=True)[i]
	InterU=np.zeros(100)
	InterR=np.zeros(100)
	InterS=np.zeros(100)
	for j in range(0,100):
		zcoord = np.linspace(-1,0,100,endpoint=True)[j]
		InterU[j]=u(i,zcoord)
		InterR[j]=rho(i,zcoord)
		InterS[j]=stream(i,zcoord)
	Uvec[i,:]=InterU
	Rvec[i,:]=InterR
	Svec[i,:]=InterS

#Plots
Rvec = np.transpose(Rvec)
Uvec = np.transpose(Uvec)
Svec = np.transpose(Svec)

plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')
cs=plt.contourf(Yvec,Zvec,Svec,25)
ct=plt.contour(Yvec,Zvec,Rvec,10,colors='k')
plt.clabel(ct, inline=1, fontsize=18)
cbar=plt.colorbar(cs)
cbar.ax.tick_params(labelsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.tick_params(axis='both', which='minor', labelsize=20)
plt.xlabel('Meridional distance',fontsize=20)
plt.ylabel('Vertical distance',fontsize=20)