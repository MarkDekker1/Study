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

#Data inladen
file = '/home/mark/Documents/LocalStudy/Datafiles/1991_1998D.nc'
ncdf = Dataset(file, mode='r')

#Variables
Lat = ncdf.variables['latitude'][:]
Lon = ncdf.variables['longitude'][:]
Thermal = ncdf.variables['ttr'][:]
Solar = ncdf.variables['tsr'][:]
Time = ncdf.variables['time'][:]

#%% Averaging

SolarM=np.zeros(shape=(181,360))
ThermalM=np.zeros(shape=(181,360))

for i in range(0,len(Time)):
	SolarM = SolarM+Solar[i]
	ThermalM = ThermalM+Thermal[i]
	
SolarM = SolarM/len(Time)/12./3600.
ThermalM = ThermalM/len(Time)/12./3600.

SolarL=np.zeros(181)
ThermalL=np.zeros(181)

for i in range(0,len(SolarM)):
	SolarL[i] = np.mean(SolarM[i,:])
	ThermalL[i] = np.mean(ThermalM[i,:])
	
SolarT=np.zeros(shape=(24,181))
ThermalT=np.zeros(shape=(24,181))
SolarTot=np.zeros(shape=(12,181))
ThermalTot=np.zeros(shape=(12,181))

for k in range(0,7):
	SolarGather=[]
	ThermalGather=[]
	for j in range(24*k+0,24*k+24):
		for i in range(0,len(SolarM)):
			SolarT[j-24*k,i] = (np.mean(Solar[j,i,:])+np.mean(Solar[j+1,i,:]))/2.
			ThermalT[j-24*k,i] = (np.mean(Thermal[j,i,:])+np.mean(Thermal[j+1,i,:]))/2.
		if j%2==0:
			SolarGather.append(SolarT[j-24*k])
			ThermalGather.append(ThermalT[j-24*k])
	SolarTot=SolarTot+SolarGather
	ThermalTot=ThermalTot+ThermalGather

SolarTot=SolarTot/7./12./3600.
ThermalTot=ThermalTot/7./12./3600.

#%% Plotting Horizontally
Lat_0=np.mean(Lat)
Lon_0=np.mean(Lon)

#Actual plot
plt.figure(num=None, figsize=(10,6),dpi=150, facecolor='w', edgecolor='k')

m = Basemap(llcrnrlon=-180,llcrnrlat=-90,urcrnrlon=180,urcrnrlat=90,
            resolution='l',projection='cyl',
            lat_ts=40,lat_0=Lat_0,lon_0=Lon_0)
												
xi, yi = m(Lon, Lat)
xi, yi = np.meshgrid(xi,yi)

Colors = m.contourf(xi,yi,ThermalM,50,cmap=plt.cm.jet)

#m.fillcontinents(color='grey')
m.drawparallels(np.arange(-90., 91., 30), labels=[1,0,0,0], fontsize=25)
m.drawmeridians(np.arange(-180., 180., 60), labels=[0,0,0,1], fontsize=25)

m.drawcoastlines()
cbar = m.colorbar(Colors, location='bottom', pad="10%",extend='both')
cbar.ax.tick_params(labelsize=20) 
plt.show()

#%% Plotting Latitudonal
plt.figure(num=None, figsize=(10,6),dpi=250, facecolor='w', edgecolor='k')

plt.plot(Lat,np.zeros(len(Lat)),'k--',linewidth=3)
plt.plot(Lat,SolarL,linewidth=3)
plt.plot(Lat,-ThermalL,linewidth=3)
plt.plot(Lat,SolarL+ThermalL,linewidth=3)
plt.xlabel('Latitude',fontsize=20)
plt.ylabel('Radiation (W/m2)',fontsize=20)
plt.xlim([-90,90])
plt.ylim([-150,350])
plt.tick_params(axis='both', which='major', labelsize=20)
plt.tick_params(axis='both', which='minor', labelsize=20)

#%% Plotting Temporal
plt.figure(num=None, figsize=(10,6),dpi=250, facecolor='w', edgecolor='k')

Colors= plt.contourf(Lat,np.linspace(0,12,12,endpoint=True),SolarTot+ThermalTot,25)
plt.xlabel('Latitude',fontsize=20)
plt.ylabel('Month',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.tick_params(axis='both', which='minor', labelsize=20)
plt.colorbar(Colors)
cbar.ax.tick_params(labelsize=20) 