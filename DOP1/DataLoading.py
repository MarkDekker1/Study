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
file = 'C:\Users\Rob\Documents\Studie Mark\Dynamical Oceanography\GRIDONE_1D.nc'
ncdf = Dataset(file, mode='r')
file2 = 'C:\Users\Rob\Documents\Studie Mark\Dynamical Oceanography\DATAWIND.nc'
ncdf2 = Dataset(file2, mode='r')

#Uithalen variabelen
Lat = ncdf.variables['y_range'][:]
Lon = ncdf.variables['x_range'][:]
Dim = ncdf.variables['dimension'][:]
Sp = ncdf.variables['spacing'][:]
Depth = ncdf.variables['z']

Lat2 = ncdf2.variables['latitude'][:]
Lon2 = ncdf2.variables['longitude'][:]
Time = ncdf2.variables['time'][:]

#Berekenen gemiddelde snelheden
U=ncdf2.variables['u10'][0][:][:]
for i in range(1,len(Time)):
    U = U+ncdf2.variables['u10'][i][:][:]

U=U/len(Time)

V=ncdf2.variables['v10'][0][:][:]
for i in range(1,len(Time)):
    V = V+ncdf2.variables['v10'][i][:][:]

V=V/len(Time)