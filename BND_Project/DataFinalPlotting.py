import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.mlab import bivariate_normal
from matplotlib.ticker import LogFormatter


#%% FLux
fig, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True,sharex=True, figsize=(14,8),dpi=500)

b1=-200
b2=200
Colorlevels=np.linspace(b1,b2,100,endpoint=True)
#Colorlevels=[b1,b1/2,b1/5,b1/10,b1/100,0,b2/100,b2/10,b2/5,b2/2,b2]
Edges1=np.linspace(b2,100000000,2,endpoint=True)
Edges2=np.linspace(-100000000,b1,2,endpoint=True)
#norm = colors.BoundaryNorm(boundaries=Colorlevels, ncolors=256)


cs1=ax1.contourf(Lat,Timevec,Flux_315K,levels=Colorlevels,cmap=cm.seismic)
cs1=ax1.contourf(Lat,Timevec,Flux_315K,levels=Edges1,colors='DarkRed')
cs1=ax1.contourf(Lat,Timevec,Flux_315K,levels=Edges2,colors='DarkBlue')
CS=ax1.contour(Lat,Timevec,Flux_315K,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.tick_params(axis='both', which='minor', labelsize=20)
ax1.set_ylabel('Time in days', fontsize=20)

Timevec=np.linspace(1,178,178)/2
cs2=ax2.contourf(Lat,Timevec,Flux_350K,levels=Colorlevels,cmap=cm.seismic)
cs2=ax2.contourf(Lat,Timevec,Flux_350K,levels=Edges1,colors='DarkRed')
cs2=ax2.contourf(Lat,Timevec,Flux_350K,levels=Edges2,colors='DarkBlue')
CS=ax2.contour(Lat,Timevec,Flux_350K,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax2.tick_params(axis='both', which='major', labelsize=20)
ax2.set_xlabel('Latitude', fontsize=20)

Timevec=np.linspace(1,179,179)/2
cs3=ax3.contourf(Lat,Timevec,np.array(Flux_600K)*100,levels=Colorlevels,cmap=cm.seismic)
CS=ax3.contour(Lat,Timevec,np.array(Flux_600K)*100,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax3.tick_params(axis='both', which='major',labelsize=20)

ax3.set_xticks([0,30,60,90])

cax = fig.add_axes([0.12, -0.02, 0.79, 0.05])
cbar=fig.colorbar(cs3, cax=cax,orientation='horizontal',spacing='uniform',ticks=[-250,-200,-150,-100,-50,0,50,100,150,200,250],extend='both')
cbar.ax.tick_params(labelsize=15) 
cbar.ax.set_xlabel('Isentropic Mass flux',fontsize=20) 

#%% S
fig, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True,sharex=True, figsize=(14,8))

b1=0.
b2=2
Colorlevels=np.linspace(b1,b2,25,endpoint=True)
Edges1=np.linspace(b2,100000000,2,endpoint=True)
Edges2=np.linspace(-100000000,b1,2,endpoint=True)


cs1=ax1.contourf(Lat,Timevec,np.array(S_315K)/np.mean(S_315K),levels=Colorlevels,cmap=cm.coolwarm)
CS=ax1.contour(Lat,Timevec,S_315K,levels=[1,10,50,100,150],linewidth=3.0,colors='k')
plt.clabel(CS, fontsize=13, inline=1,fmt='%1.0f')

ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.tick_params(axis='both', which='minor', labelsize=20)
ax1.set_ylabel('Time in days', fontsize=20)

Timevec=np.linspace(1,178,178)/2
cs2=ax2.contourf(Lat,Timevec,np.array(S_350K)/np.mean(S_350K),levels=Colorlevels,cmap=cm.coolwarm)
cs2=ax2.contourf(Lat,Timevec,np.array(S_350K)/np.mean(S_350K),levels=Edges1,colors='DarkRed')
cs2=ax2.contourf(Lat,Timevec,np.array(S_350K)/np.mean(S_350K),levels=Edges2,colors='DarkBlue')
CS=ax2.contour(Lat,Timevec,S_350K,levels=[1,25,50,75],linewidth=3.0,colors='k')
plt.clabel(CS, fontsize=13, inline=1,fmt='%1.0f')

ax2.tick_params(axis='both', which='major', labelsize=20)
ax2.set_xlabel('Latitude', fontsize=20)

Timevec=np.linspace(1,179,179)/2
cs3=ax3.contourf(Lat,Timevec,np.array(S_600K)/np.mean(S_600K),levels=Colorlevels,cmap=cm.coolwarm)
CS=ax3.contour(Lat,Timevec,np.array(S_600K),levels=[1.5,2],linewidth=3.0,colors='k')
plt.clabel(CS, fontsize=13, inline=1,fmt='%1.1f')

ax3.tick_params(axis='both', which='major',labelsize=20)

ax3.set_xticks([0,30,60,90])

cax = fig.add_axes([0.12, -0.02, 0.79, 0.05])
cbar=fig.colorbar(cs3, cax=cax,orientation='horizontal',spacing='uniform')
cbar.ax.tick_params(labelsize=15) 
cbar.ax.set_xlabel('Normalized Isentropic Density',fontsize=20) 

#%% V
fig, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True,sharex=True, figsize=(14,8))

b1=-2.
b2=4.
Colorlevels=np.linspace(b1,b2,100,endpoint=True)
Edges1=np.linspace(b2,100000000,2,endpoint=True)
Edges2=np.linspace(-100000000,b1,2,endpoint=True)


cs1=ax1.contourf(Lat,Timevec,V_315K,levels=Colorlevels)
CS=ax1.contour(Lat,Timevec,V_315K,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.tick_params(axis='both', which='minor', labelsize=20)
ax1.set_ylabel('Time [days]', fontsize=20)

Timevec=np.linspace(1,178,178)/2
cs2=ax2.contourf(Lat,Timevec,V_350K,levels=Colorlevels)
cs2=ax2.contourf(Lat,Timevec,V_350K,levels=Edges1,colors='DarkRed')
cs2=ax2.contourf(Lat,Timevec,V_350K,levels=Edges2,colors='DarkBlue')
CS=ax2.contour(Lat,Timevec,V_350K,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax2.tick_params(axis='both', which='major', labelsize=20)
ax2.set_xlabel('Latitude', fontsize=20)

Timevec=np.linspace(1,179,179)/2
cs3=ax3.contourf(Lat,Timevec,V_600K,levels=Colorlevels)
CS=ax3.contour(Lat,Timevec,V_600K,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax3.tick_params(axis='both', which='major',labelsize=20)

ax3.set_xticks([0,30,60,90])

cax = fig.add_axes([0.12, -0.02, 0.79, 0.05])
cbar=fig.colorbar(cs3, cax=cax,orientation='horizontal',ticks=[-3,-2,-1,0,1,2,3,4,5])
cbar.ax.tick_params(labelsize=15) 
cbar.ax.set_xlabel('Meridional Velocity [m/s]',fontsize=20) 