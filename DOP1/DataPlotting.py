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

#Preambule plots
Lon_0 = 0.
Lat_0 = 0.

lon, lat = np.meshgrid(Lon2, Lat2)

#%% Plot Streamfunction

# Limits
lim1=-1e4
lim2=1e4

#Actual plot
plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
xi, yi = m(lon, lat)

v = np.linspace(lim1,lim2,101,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)

m.contour(xi,yi,Stream,levels=([0]),colors='grey')
m.contourf(xi,yi,Stream,levels=v2,colors='maroon')
m.contourf(xi,yi,Stream,levels=v3,colors='navy')
Colors = m.contourf(xi,yi,Stream,levels=v,cmap=plt.cm.jet)

r=5
m.quiver(xi[::r,::r],yi[::r,::r],VelocityU[::r,::r]/VelocityT[::r,::r],VelocityV[::r,::r]/VelocityT[::r,::r],color='k',headlength=7,scale=40)
#m.streamplot(xi,yi,VelocityU,VelocityV,color=VelocityT,cmap=cm.cool,linewidth=2,arrowstyle='->',arrowsize=1.5)
        
m.fillcontinents(color='grey')
m.drawparallels(np.arange(10., 71., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()
cbar = m.colorbar(Colors, extend='both', location='bottom',pad="10%")
plt.show()

#%% Plot Meridional Velocity

# Limits
lim1=-1e-4
lim2=1e-4

# Actual plot
plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
xi, yi = m(lon, lat)

v = np.linspace(lim1,lim2,21,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)

m.contourf(xi,yi,VelocityV,levels=v2,colors='DarkRed')
m.contourf(xi,yi,VelocityV,levels=v3,colors='DarkBlue')
Colors = m.contourf(xi,yi,VelocityV,levels=v,cmap=plt.cm.jet)
        
m.fillcontinents(color='grey')
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(Colors, extend='both', location='bottom',pad="10%")
plt.show()

#%% Plot Zonal Velocity

# Limits
lim1=-5e-2
lim2=5e-2

# Actual plot
plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
xi, yi = m(lon, lat)

v = np.linspace(lim1,lim2,21,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)

m.contourf(xi,yi,VelocityU,levels=v2,colors='DarkRed')
m.contourf(xi,yi,VelocityU,levels=v3,colors='DarkBlue')
Colors = m.contourf(xi,yi,VelocityU,levels=v,cmap=plt.cm.jet)
        
m.fillcontinents(color='grey')
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(Colors, extend='both', location='bottom',pad="10%")
plt.show()

#%% Plot Total Velocity

# Limits
lim1=0
lim2=1e-1

# Actual plot
plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
xi, yi = m(lon, lat)

v = np.linspace(lim1,lim2,21,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)

m.contourf(xi,yi,VelocityT,levels=v2,colors='DarkRed')
m.contourf(xi,yi,VelocityT,levels=v3,colors='DarkBlue')
Colors = m.contourf(xi,yi,VelocityT,levels=v,cmap=plt.cm.jet)
        
m.fillcontinents(color='grey')
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(Colors, extend='both', location='bottom',pad="10%")
plt.show()

#%% Plot Stress

# Limits
lim1=-1e-2
lim2=1e-2

# Actual plot
plt.figure(num=None, figsize=(7,7),dpi=300, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
xi, yi = m(lon, lat)

v = np.linspace(lim1,lim2,51,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)

m.contourf(xi,yi,Vstress,levels=v2,colors='DarkRed')
m.contourf(xi,yi,Vstress,levels=v3,colors='DarkBlue')
Colors = m.contourf(xi,yi,Vstress,levels=v,cmap=plt.cm.jet)
        
m.fillcontinents(color='grey')
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(Colors, extend='both', location='bottom',pad="10%")
plt.show()