#Packages
from netCDF4 import Dataset
from pylab import * 

#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import scipy

#%%Data inladen (verschilt per computer!)
file = 'C:\Users\Rob\Documents\Localstudy\BoundaryLayers\DataIsentropicMassFluxTh.nc'
ncdf = Dataset(file, mode='r')
file2 = 'C:\Users\Rob\Documents\Localstudy\BoundaryLayers\Data2010.nc'
#file2 = '\Data_2010.nc'
ncdf2 = Dataset(file2, mode='r')

#%%Uithalen variabelen
Lat = ncdf.variables['latitude'][:]
Lon = ncdf.variables['longitude'][:]
Time = ncdf.variables['time'][:]
Levels = ncdf.variables['level'][:]
Time2=ncdf2.variables['time'][:]
#Levels=Levels[::-1]

def ZonalmeanP(Thlev,tlev,latlev):
    return np.mean(ncdf.variables['pres'][tlev][Thlev][latlev][:])

def ZonalmeanV(Thlev,tlev,latlev):
    return np.mean(ncdf.variables['v'][tlev][Thlev][latlev][:])
    
def ZonalmeanSigma(Thlev,tlev,latlev):
    DeltaTh = Levels[Thlev+1]-Levels[Thlev-1]
    Deltap = ZonalmeanP(Thlev+1,tlev,latlev)-ZonalmeanP(Thlev-1,tlev,latlev)
    return -1./g * Deltap/DeltaTh   
#%%
Tpoint=1
Ppoint=3
Pref = 1000.
Rcp = 0.286
#Theta = Temp*(Pref/Ppoint)**Rcp
g=9.81
Vvec=[]
Svec=[]
Fvec=[]
for i in range(0,5):
    Vvec2=[]
    Svec2=[]
    for th in range(1,14):
        Vvec3=[]
        Svec3=[]
        for y in range(0,91):
            Vvec3.append(ZonalmeanV(th,i*10,y))
            Svec3.append(ZonalmeanSigma(th,i*10,y))
        Vvec2.append(Vvec3)
        Svec2.append(Svec3)
        print th
    Vvec.append(Vvec2)
    Svec.append(Svec2)
    Fvec.append(np.array(Vvec[i])*np.array(Svec[i]))
    print i
    

#%%
T=4
A=Fvec[T]

b1=-100
b2=100
Colorlevels=np.linspace(b1,b2,100,endpoint=True)
Edges1=np.linspace(b2,100000000,2,endpoint=True)
Edges2=np.linspace(-100000000,b1,2,endpoint=True)

fig=plt.figure(num=None, figsize=(6,8),dpi=150, facecolor='w', edgecolor='k')
cs=plt.contourf(Lat,Levels[1:14],A,levels=Colorlevels,cmap=cm.seismic)
cs1=plt.contourf(Lat,Levels[1:14],A,levels=Edges1,colors='DarkRed')
cs1=plt.contourf(Lat,Levels[1:14],A,levels=Edges2,colors='DarkBlue')
CS=plt.contour(Lat,Levels[1:14],A,levels=[-1000,0,1000],linewidth=3.0,colors='k')

#plt.title('Isentropic Mass Flux (mean part)')
plt.xlabel('Latitude',fontsize=16)
plt.ylabel('Potential temperature',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.tick_params(axis='both', which='minor', labelsize=16)
cax = fig.add_axes([0.12, -0.02, 0.79, 0.05])
cbar=fig.colorbar(cs, cax=cax,orientation='horizontal',spacing='uniform',ticks=[-250,-200,-150,-100,-50,0,50,100,150,200,250],extend='both')
cbar.ax.tick_params(labelsize=15) 


