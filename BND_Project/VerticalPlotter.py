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
    
    
def ZonalmeanP(Thlev,tlev,latlev):
    return np.mean(ncdf.variables['pres'][tlev][Thlev][latlev][:])
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
Pvec=[]
for i in range(0,1):
    Vvec2=[]
    Svec2=[]
    Pvec2=[]
    for th in range(1,14):
        Vvec3=[]
        Svec3=[]
        Pvec3=[]
        for y in range(0,91):
            Vvec3.append(ZonalmeanV(th,i*10,y))
            Svec3.append(ZonalmeanSigma(th,i*10,y))
            Pvec3.append(ZonalmeanP(th,i*10,y))
        Vvec2.append(Vvec3)
        Svec2.append(Svec3)
        Pvec2.append(Pvec3)
        print th
    Vvec.append(Vvec2)
    Svec.append(Svec2)
    Pvec.append(Pvec2)
    Fvec.append(np.array(Vvec[i])*np.array(Svec[i]))
    print i
    

#%%
T=0
A=Fvec[T]
P=Pvec[T]

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
CS=plt.contour(Lat,Levels[1:14],P,levels=[3000,6000,9000,12000,20000,50000,90000],linewidth=5.0,colors='gray')

#plt.title('Meridional velocity')
plt.xlabel('Latitude',fontsize=16)
plt.ylabel('Potential temperature',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.tick_params(axis='both', which='minor', labelsize=16)
cax = fig.add_axes([0.12, -0.02, 0.79, 0.05])
cbar=fig.colorbar(cs, cax=cax,orientation='horizontal',spacing='uniform',ticks=[-150,-100,-50,0,50,100,150],extend='both')
cbar.ax.tick_params(labelsize=15) 
cbar.ax.set_xlabel('Zonal mean isentropic mass flux (mean)',fontsize=20) 


#%%

fig, (ax1, ax2, ax3,ax4,ax5) = plt.subplots(1,5,sharey=True,sharex=True, figsize=(17,8),dpi=500)
T=4
A_1=Fvec[0]
A_2=Fvec[1]
A_3=Fvec[2]
A_4=Fvec[3]
A_5=Fvec[4]

b1=-75
b2=75
Colorlevels=np.linspace(b1,b2,100,endpoint=True)
Edges1=np.linspace(b2,100000000,2,endpoint=True)
Edges2=np.linspace(-100000000,b1,2,endpoint=True)
ax3.set_xlabel('Latitude',fontsize=16)
ax1.set_ylabel('Potential temperature', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=16)
ax1.tick_params(axis='both', which='minor', labelsize=16)
ax2.tick_params(axis='both', which='major', labelsize=16)
ax2.tick_params(axis='both', which='minor', labelsize=16)
ax3.tick_params(axis='both', which='major', labelsize=16)
ax3.tick_params(axis='both', which='minor', labelsize=16)
ax4.tick_params(axis='both', which='major', labelsize=16)
ax4.tick_params(axis='both', which='minor', labelsize=16)
ax5.tick_params(axis='both', which='major', labelsize=16)
ax5.tick_params(axis='both', which='minor', labelsize=16)


#AX1
cs=ax1.contourf(Lat,Levels[1:14],A_1,levels=Colorlevels,cmap=cm.seismic)
cs1=ax1.contourf(Lat,Levels[1:14],A_1,levels=Edges1,colors='DarkRed')
cs1=ax1.contourf(Lat,Levels[1:14],A_1,levels=Edges2,colors='DarkBlue')
CS=ax1.contour(Lat,Levels[1:14],A_1,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#AX2
cs=ax2.contourf(Lat,Levels[1:14],A_2,levels=Colorlevels,cmap=cm.seismic)
cs1=ax2.contourf(Lat,Levels[1:14],A_2,levels=Edges1,colors='DarkRed')
cs1=ax2.contourf(Lat,Levels[1:14],A_2,levels=Edges2,colors='DarkBlue')
CS=ax2.contour(Lat,Levels[1:14],A_2,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#AX3
cs=ax3.contourf(Lat,Levels[1:14],A_3,levels=Colorlevels,cmap=cm.seismic)
cs1=ax3.contourf(Lat,Levels[1:14],A_3,levels=Edges1,colors='DarkRed')
cs1=ax3.contourf(Lat,Levels[1:14],A_3,levels=Edges2,colors='DarkBlue')
CS=ax3.contour(Lat,Levels[1:14],A_3,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#AX4
cs=ax4.contourf(Lat,Levels[1:14],A_4,levels=Colorlevels,cmap=cm.seismic)
cs1=ax4.contourf(Lat,Levels[1:14],A_4,levels=Edges1,colors='DarkRed')
cs1=ax4.contourf(Lat,Levels[1:14],A_4,levels=Edges2,colors='DarkBlue')
CS=ax4.contour(Lat,Levels[1:14],A_4,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#AX3
cs=ax5.contourf(Lat,Levels[1:14],A_5,levels=Colorlevels,cmap=cm.seismic)
cs1=ax5.contourf(Lat,Levels[1:14],A_5,levels=Edges1,colors='DarkRed')
cs1=ax5.contourf(Lat,Levels[1:14],A_5,levels=Edges2,colors='DarkBlue')
CS=ax5.contour(Lat,Levels[1:14],A_5,levels=[-1000,0,1000],linewidth=3.0,colors='k')



ax1.set_xticks([0,30,60,90])
ax2.set_xticks([0,30,60,90])
ax3.set_xticks([0,30,60,90])
ax4.set_xticks([0,30,60,90])
ax5.set_xticks([0,30,60,90])

cax = fig.add_axes([0.12, -0.02, 0.79, 0.05])
cbar=fig.colorbar(cs, cax=cax,orientation='horizontal',spacing='uniform',ticks=[-250,-200,-150,-100,-50,0,50,100,150,200,250],extend='both')
cbar.ax.tick_params(labelsize=15) 
