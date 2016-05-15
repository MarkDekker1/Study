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

Lat = np.arange(-90.,91.,1.)
Lon = np.arange(-180.,181.,1.)
Lat3 = np.arange(-90.,91.,1.)
Lon3 = np.arange(-180.,178.,1.)

lon, lat = np.meshgrid(Lon, Lat)
xi, yi = m(lon, lat)
yi=yi[::-1]

lon2, lat2 = np.meshgrid(Lon2, Lat2)
xi2, yi2 = m(lon2, lat2)

# Limits
lim1=-10e3
lim2=10e3

# Plot Streamfunction
plt.figure(num=None, figsize=(8, 8), dpi=100, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-90,llcrnrlat=0,urcrnrlon=30,urcrnrlat=70,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
m.fillcontinents(color='grey')

v = np.linspace(lim1,lim2,11,endpoint=True)
v2 = np.linspace(lim2,10000000,4,endpoint=True)
v3 = np.linspace(-100000000,lim1,4,endpoint=True)

m.contour(xi,yi,Dtot,3,linestyle='-',colors='k')
m.contourf(xi2,yi2,Stream,levels=v2,colors='DarkRed')
m.contourf(xi2,yi2,Stream,levels=v3,colors='DarkBlue')
Colors = m.contourf(xi2,yi2,Stream,levels=v,cmap=plt.cm.jet)
        
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=12)
m.drawmeridians(np.arange(-180., 180., 30), labels=[0,0,0,1], fontsize=12)

m.drawcoastlines()

cbar = m.colorbar(cs, extend='both', location='bottom',pad="10%")
plt.show()