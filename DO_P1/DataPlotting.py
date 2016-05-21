#Packages
from netCDF4 import Dataset
from pylab import * 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
from matplotlib.colors import BoundaryNorm
from matplotlib.colors import LogNorm
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import scipy
import matplotlib.colors as colors

#Preambule plots
Lon_0 = 0.
Lat_0 = 0.

lon, lat = np.meshgrid(Lon2, Lat2)

#%% Plot Streamfunction

# Limits
lim1=-1e5
lim2=1e5

#Actual plot
plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
xi, yi = m(lon, lat)

v = np.linspace(lim1,lim2,200,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)
vlog=[lim1,lim1/5,lim1/10,lim1/100,0,lim2/100,lim2/10,lim2/5,lim2]

bnorm = BoundaryNorm(vlog, ncolors=250, clip=False)

m.contour(xi,yi,Stream,levels=([-4000,0,20000]),colors='grey')
m.contourf(xi,yi,Stream,levels=v2,colors='maroon')
m.contourf(xi,yi,Stream,levels=v3,colors='navy')

Colors = m.contourf(xi,yi,Stream,levels=v,cmap=plt.cm.jet,norm=colors.SymLogNorm(linthresh=500, linscale=1e-10,vmin=-200000, vmax=200000,clip=False))

r=5
#m.quiver(xi[::r,::r],yi[::r,::r],VelocityU[::r,::r]/VelocityT[::r,::r],VelocityV[::r,::r]/VelocityT[::r,::r],color='k',headlength=7,scale=40)
        
m.fillcontinents(color='grey')
m.drawparallels(np.arange(10., 71., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()
cbar = m.colorbar(Colors,spacing='log',ticks=[-100000,-10000,-1000,0,1000,10000,100000], location='bottom', pad="10%")
plt.show()

#%% Plot Meridional Velocity

# Limits
lim1=-2e-3
lim2=2e-3

# Actual plot
plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
xi, yi = m(lon, lat)

v = np.linspace(lim1,lim2,200,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)

m.contour(xi,yi,VelocityV,levels=([0]),colors='grey')
m.contourf(xi,yi,VelocityV,levels=v2,colors='DarkRed')
m.contourf(xi,yi,VelocityV,levels=v3,colors='DarkBlue')
Colors = m.contourf(xi,yi,VelocityV,levels=v,cmap=plt.cm.jet,norm=colors.SymLogNorm(linthresh=0.0004, linscale=1000,vmin=lim1,vmax=lim2))
        
m.fillcontinents(color='grey')
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(Colors, spacing= 'log',ticks=[lim1,lim1/10,0,lim2/10,lim2], location='bottom',pad="10%")
plt.show()

#%% Plot Zonal Velocity

# Limits
lim1=-8e-2
lim2=8e-2

# Actual plot
plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=10,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
xi, yi = m(lon, lat)

v = np.linspace(lim1,lim2,100,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)

m.contour(xi,yi,VelocityU,levels=([0]),colors='grey')
m.contourf(xi,yi,VelocityU,levels=v2,colors='DarkRed')
m.contourf(xi,yi,VelocityU,levels=v3,colors='DarkBlue')
Colors = m.contourf(xi,yi,VelocityU,levels=v,cmap=plt.cm.jet,norm=colors.SymLogNorm(linthresh=0.05, linscale=10,vmin=lim1,vmax=lim2))
        
m.fillcontinents(color='grey')
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(Colors, spacing= 'log',ticks=[lim1,lim1/10,0,lim2/10,lim2],extend='both', location='bottom',pad="10%")
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