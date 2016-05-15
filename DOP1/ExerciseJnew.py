#%% Preambule and Data loading
from netCDF4 import Dataset
import os
from pylab import * 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
#from mpl_toolkits.basemap import Basemap, cm

#Inladen data
file = 'C:\Users\Rob\Documents\Studie Mark\Dynamical Oceanography\GRIDONE_1D.nc'
ncdf = Dataset(file, mode='r')
file2 = 'C:\Users\Rob\Documents\Studie Mark\Dynamical Oceanography\DATAWIND.nc'
ncdf2 = Dataset(file2, mode='r')
def running_sum(s, n):
    return [sum(s[lo:lo + n]) for lo in range(len(s) - n + 1)]

#%%

#Uithalen van de variabelen
Lat = ncdf.variables['y_range'][:]
Lon = ncdf.variables['x_range'][:]
Dim = ncdf.variables['dimension'][:]
Sp = ncdf.variables['spacing'][:]
Depth = ncdf.variables['z']
Depthmatrix=[]

#%%
Lat2 = ncdf2.variables['latitude'][:]
Lon2 = ncdf2.variables['longitude'][:]
Time = ncdf2.variables['time'][:]

#%%
U=ncdf2.variables['u10'][0][:][:]
for i in range(1,len(Time)):
    U = U+ncdf2.variables['u10'][i][:][:]

U=U/len(Time)

#%%
V=ncdf2.variables['v10'][0][:][:]
for i in range(1,len(Time)):
    V = V+ncdf2.variables['v10'][i][:][:]

V=V/len(Time)

#%%Create matrix
#Dummyvec=[]
#for i in range(0,10801):
#    for j in range(0,21601):
#        Dummyvec.append(Depth[j])
#    Depthmatrix.append(Dummyvec)

#%% Create Depthmatrix
#Depthmat=np.reshape(Depth, (-1, 2))
Depthmat=[]
for i in range(0,10801):
    Depthmat.append(-Depth[0+21601*i:21601+21601*i:60])
#%% Redefine Lon and Lat
Lon_0 = 0.
Lat_0 = 0.

Lat = np.arange(-90.,91.,1.)
Lon = np.arange(-180.,181.,1.)
Lat3 = np.arange(-90.,91.,1.)
Lon3 = np.arange(-180.,178.,1.)

Vtot=np.sqrt(U**2+V**2)

#%%
Dtot=Depthmat[0:10801:60]

#%%
import scipy
Cd=0.001
rhoa=1.225
rhow=1000.
Ustress=rhoa*Cd*U**2*U/abs(U)
Vstress=rhoa*Cd*V**2*V/abs(V)
rhow=1000.
beta0=2*10**(-11)
Curlstress=gradient(Vstress)[0]-np.transpose(gradient(np.transpose(Ustress))[0])
MassTransport=Curlstress/beta0
A=Dtot
A=scipy.delete(A,1,1)
VelocityV=Curlstress/(beta0*rhow*A)


#%%
Bvec=[]
for i in range(0,181):
    Boundary=0.
    k=150
    while A[i][k]>0 and k<359:
        Boundary=k
        k=k+1      
    Bvec.append(Boundary)
#Bvec=Bvec[::-1]\
#%%
def xlen(latitude):
    return abs(6400000*2*np.pi/360*sin((latitude-90)/360.*2.*np.pi))
#%%
Curlstressvec=[]
Stream=np.zeros(shape=(181,360))
for i in range(0,181):
    phi=i-90.
    xlength=xlen(phi)
    ylength=1./360.*2.*np.pi*6400000.
    Curlstressvec.append(gradient(Vstress[i,:])/(xlength)-np.transpose(gradient(np.transpose(Ustress)[:,i]))/ylength)
    for j in range(0,360):
        Stream[i,j]=sum(Curlstressvec[i][j:Bvec[i]])*(Bvec[i]-j)*xlength
VelocityV=np.array(Curlstressvec)/(beta0*rhow*A)
Stream=Stream/(beta0*rhow*A)
#%% Stream
plt.figure(num=None, figsize=(8, 8), dpi=100, facecolor='w', edgecolor='k')
#Map

m = Basemap(llcrnrlon=-90,llcrnrlat=0,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
m.fillcontinents(color='grey')#,lake_color='aqua')
lon, lat = np.meshgrid(Lon, Lat)
xi, yi = m(lon, lat)
lon2, lat2 = np.meshgrid(Lon2, Lat2)
xi2, yi2 = m(lon2, lat2)
lon3,lat3=np.meshgrid(Lon3,Lat3)
xi3,yi3=m(lon3,lat3)

yi=yi[::-1]

# Plot Data
lim1=-10e3
lim2=10e3
v = np.linspace(lim1,lim2,11,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)
#v = array([-100000,-50000,-25000,-10000,-7500,-5000,-2500,0,2500,5000,7500,10000,25000,50000,100000])
cs = m.contour(xi,yi,Dtot,3,linestyle='-',colors='k')
#cs = m.contour(xi,yi,Dtot,levels=np.array([0]),linestyle='-',colors='k',linewidth=10)
cs2 = m.contourf(xi2,yi2,Stream,levels=v2,colors='DarkRed')
cs2 = m.contourf(xi2,yi2,Stream,levels=v3,colors='DarkBlue')
cs = m.contourf(xi2,yi2,Stream,levels=v,cmap=plt.cm.jet)
        
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(cs, extend='both', location='bottom',pad="10%")
plt.show()
#%% Curl
plt.figure(num=None, figsize=(8, 8), dpi=100, facecolor='w', edgecolor='k')
#Map

m = Basemap(llcrnrlon=-90,llcrnrlat=0,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
#m.fillcontinents(color='grey',lake_color='aqua')
lon, lat = np.meshgrid(Lon, Lat)
xi, yi = m(lon, lat)
lon2, lat2 = np.meshgrid(Lon2, Lat2)
xi2, yi2 = m(lon2, lat2)
lon3,lat3=np.meshgrid(Lon3,Lat3)
xi3,yi3=m(lon3,lat3)

yi=yi[::-1]

# Plot Data
lim1=-10e-9
lim2=10e-9
v = np.linspace(lim1,lim2,11,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)
#v = array([-100000,-50000,-25000,-10000,-7500,-5000,-2500,0,2500,5000,7500,10000,25000,50000,100000])
#cs = m.contour(xi,yi,Dtot,3,linestyle='-',colors='k')
cs = m.contour(xi,yi,Dtot,levels=np.array([0]),linestyle='-',colors='k',linewidth=10)
cs2 = m.contourf(xi2,yi2,Curlstressvec,levels=v2,colors='DarkRed')
cs2 = m.contourf(xi2,yi2,Curlstressvec,levels=v3,colors='DarkBlue')
cs = m.contourf(xi2,yi2,Curlstressvec,levels=v,cmap=plt.cm.jet)
        
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

#m.drawcoastlines()

cbar = m.colorbar(cs, extend='both', location='bottom',pad="10%")
plt.show()
#%% Velo
plt.figure(num=None, figsize=(8, 8), dpi=100, facecolor='w', edgecolor='k')
#Map

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=40,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
m.fillcontinents(color='grey',lake_color='aqua')
lon, lat = np.meshgrid(Lon, Lat)
xi, yi = m(lon, lat)
lon2, lat2 = np.meshgrid(Lon2, Lat2)
xi2, yi2 = m(lon2, lat2)
lon3,lat3=np.meshgrid(Lon3,Lat3)
xi3,yi3=m(lon3,lat3)

yi=yi[::-1]
lim1=-10e-5
lim2=10e-5
v = np.linspace(lim1,lim2,11,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)
#v = array([-100000,-50000,-25000,-10000,-7500,-5000,-2500,0,2500,5000,7500,10000,25000,50000,100000])
cs = m.contour(xi,yi,Dtot,3,linestyle='-',colors='k')
cs2 = m.contourf(xi2,yi2,VelocityV,levels=v2,colors='DarkRed')
cs2 = m.contourf(xi2,yi2,VelocityV,levels=v3,colors='DarkBlue')
cs = m.contourf(xi2,yi2,VelocityV,levels=v,cmap=plt.cm.jet)
        
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(cs, extend='both', location='bottom',pad="10%")
#cbar.set_label('Kelvin')

#plt.title('Bathymetry North-Atlantic', fontsize=14)

plt.show()
#plt.savefig('Test.png')
#%% StreamV
plt.figure(num=None, figsize=(8, 8), dpi=100, facecolor='w', edgecolor='k')
#Map

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=40,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
m.fillcontinents(color='grey',lake_color='aqua')
lon, lat = np.meshgrid(Lon, Lat)
xi, yi = m(lon, lat)
lon2, lat2 = np.meshgrid(Lon2, Lat2)
xi2, yi2 = m(lon2, lat2)
lon3,lat3=np.meshgrid(Lon3,Lat3)
xi3,yi3=m(lon3,lat3)

yi=yi[::-1]
lim1=-10e2
lim2=10e2
v = np.linspace(lim1,lim2,11,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)
#v = array([-100000,-50000,-25000,-10000,-7500,-5000,-2500,0,2500,5000,7500,10000,25000,50000,100000])
cs = m.contour(xi,yi,Dtot,3,linestyle='-',colors='k')
cs2 = m.contourf(xi2,yi2,Vmat,levels=v2,colors='DarkRed')
cs2 = m.contourf(xi2,yi2,Vmat,levels=v3,colors='DarkBlue')
cs = m.contourf(xi2,yi2,Vmat,levels=v,cmap=plt.cm.jet)
        
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(cs, extend='both', location='bottom',pad="10%")
#cbar.set_label('Kelvin')

#plt.title('Bathymetry North-Atlantic', fontsize=14)

plt.show()
#plt.savefig('Test.png')