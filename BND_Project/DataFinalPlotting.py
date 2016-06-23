import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.mlab import bivariate_normal
from matplotlib.ticker import LogFormatter
import matplotlib.cm as cm

#%% Automatic Running mean important
A=Flux_mean_600_2010
A_RM=Flux_mean_600_2010

A_RM[0]=(A[0]+0.5*A[1])/1.5
A_RM[len(A)-1]=(A[len(A)-1]+0.5*A[len(A)-2])/1.5

for i in range(1,len(A)-1):
    A_RM[i]=(0.5*A[i-1]+A[i]+0.5*A[i+1])/2.

#%%
RefM_315_2010=Flux_mean_315_2010[0:180:2]
RefM_315_2007=Flux_mean_315_2007[0:180:2]
RefM_350_2010=Flux_mean_350_2010[0:180:2]
RefM_350_2007=Flux_mean_350_2007[0:180:2]
RefM_600_2007=Flux_mean_600_2007[0:180:2]
RefM_600_2010=Flux_mean_600_2010[0:180:2]


SM_600_2007=S_mean_600_2007[0:180:2]
#%% Automatic plotter

Title='Isentropic Mass Flux'
B_1=Flux_mean_315_2010
B_2=Flux_mean_350_2010
B_3=np.array(Flux_mean_600_2010)*10
D_3=SM_600_2007
Lat=np.linspace(0,90,91,endpoint=True)
Lat=Lat[::-1]
Timevec1=np.linspace(1,180,180,endpoint=True)/2
Timevec2=np.linspace(1,180,180,endpoint=True)/2
Timevec3=np.linspace(1,180,180,endpoint=True)/2


fig, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True,sharex=True, figsize=(14,8),dpi=500)

b1=-200
b2=200
Colorlevels=np.linspace(b1,b2,100,endpoint=True)
#Colorlevels=[b1,b1/2,b1/5,b1/10,b1/100,0,b2/100,b2/10,b2/5,b2/2,b2]
Edges1=np.linspace(b2,100000000,2,endpoint=True)
Edges2=np.linspace(-100000000,b1,2,endpoint=True)
#norm = colors.BoundaryNorm(boundaries=Colorlevels, ncolors=256)

cs1=ax1.contourf(Lat,Timevec1,B_1,levels=Colorlevels,cmap=cm.seismic)
cs1=ax1.contourf(Lat,Timevec1,B_1,levels=Edges1,colors='DarkRed')
cs1=ax1.contourf(Lat,Timevec1,B_1,levels=Edges2,colors='DarkBlue')
CS=ax1.contour(Lat,Timevec1,B_1,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.tick_params(axis='both', which='minor', labelsize=20)
ax1.set_ylabel('Time in days', fontsize=20)

cs2=ax2.contourf(Lat,Timevec2,B_2,levels=Colorlevels,cmap=cm.seismic)
cs2=ax2.contourf(Lat,Timevec2,B_2,levels=Edges1,colors='DarkRed')
cs2=ax2.contourf(Lat,Timevec2,B_2,levels=Edges2,colors='DarkBlue')
CS=ax2.contour(Lat,Timevec2,B_2,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax2.tick_params(axis='both', which='major', labelsize=20)
ax2.set_xlabel('Latitude', fontsize=20)

cs3=ax3.contourf(Lat,Timevec3,B_3,levels=Colorlevels,cmap=cm.seismic)
CS=ax3.contour(Lat,Timevec3,B_3,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#CS=ax3.contour(Lat,Timevec3,D_3,levels=[-1000,1.5,1000],linewidth=3.0,colors='k')

ax3.tick_params(axis='both', which='major',labelsize=20)

ax3.set_xticks([0,30,60,90])

cax = fig.add_axes([0.12, -0.02, 0.79, 0.05])
cbar=fig.colorbar(cs3, cax=cax,orientation='horizontal',spacing='uniform',ticks=[-250,-200,-150,-100,-50,0,50,100,150,200,250],extend='both')
cbar.ax.tick_params(labelsize=15) 
cbar.ax.set_xlabel(Title,fontsize=20) 



#%% Runningmean Flux
Flux_315K_RM=Flux_315K

Flux_315K_RM[0]=(Flux_315K[0]+0.5*Flux_315K[1])/1.5
Flux_315K_RM[len(Flux_315K)-1]=(Flux_315K[len(Flux_315K)-1]+0.5*Flux_315K[len(Flux_315K)-2])/1.5

for i in range(1,len(Flux_315K)-1):
    Flux_315K_RM[i]=(0.5*Flux_315K[i-1]+Flux_315K[i]+0.5*Flux_315K[i+1])/2.

Flux_350K_RM=Flux_350K

Flux_350K_RM[0]=(Flux_350K[0]+0.5*Flux_350K[1])/1.5
Flux_350K_RM[len(Flux_350K)-1]=(Flux_350K[len(Flux_350K)-1]+0.5*Flux_350K[len(Flux_350K)-2])/1.5

for i in range(1,len(Flux_350K)-1):
    Flux_350K_RM[i]=(0.5*Flux_350K[i-1]+Flux_350K[i]+0.5*Flux_350K[i+1])/2.

Flux_600K_RM=Flux_600K

Flux_600K_RM[0]=(Flux_600K[0]+0.5*Flux_600K[1])/1.5
Flux_600K_RM[len(Flux_600K)-1]=(Flux_600K[len(Flux_600K)-1]+0.5*Flux_600K[len(Flux_600K)-2])/1.5

for i in range(1,len(Flux_600K)-1):
    Flux_600K_RM[i]=(0.5*Flux_600K[i-1]+Flux_600K[i]+0.5*Flux_600K[i+1])/2.

#%% Running mean V

V_315K_RM=V_315K

V_315K_RM[0]=(V_315K[0]+0.5*V_315K[1])/1.5
V_315K_RM[len(V_315K)-1]=(V_315K[len(V_315K)-1]+0.5*V_315K[len(V_315K)-2])/1.5

for i in range(1,len(V_315K)-1):
    V_315K_RM[i]=(0.5*V_315K[i-1]+V_315K[i]+0.5*V_315K[i+1])/2.

V_350K_RM=V_350K

V_350K_RM[0]=(V_350K[0]+0.5*V_350K[1])/1.5
V_350K_RM[len(V_350K)-1]=(V_350K[len(V_350K)-1]+0.5*V_350K[len(V_350K)-2])/1.5

for i in range(1,len(V_350K)-1):
    V_350K_RM[i]=(0.5*V_350K[i-1]+V_350K[i]+0.5*V_350K[i+1])/2.

V_600K_RM=V_600K

V_600K_RM[0]=(V_600K[0]+0.5*V_600K[1])/1.5
V_600K_RM[len(V_600K)-1]=(V_600K[len(V_600K)-1]+0.5*V_600K[len(V_600K)-2])/1.5

for i in range(1,len(V_600K)-1):
    V_600K_RM[i]=(0.5*V_600K[i-1]+V_600K[i]+0.5*V_600K[i+1])/2.

#%% Running mean V

S_315K_RM=S_315K

S_315K_RM[0]=(S_315K[0]+0.5*S_315K[1])/1.5
S_315K_RM[len(S_315K)-1]=(S_315K[len(S_315K)-1]+0.5*S_315K[len(S_315K)-2])/1.5

for i in range(1,len(S_315K)-1):
    S_315K_RM[i]=(0.5*S_315K[i-1]+S_315K[i]+0.5*S_315K[i+1])/2.

S_350K_RM=S_350K

S_350K_RM[0]=(S_350K[0]+0.5*S_350K[1])/1.5
S_350K_RM[len(S_350K)-1]=(S_350K[len(S_350K)-1]+0.5*S_350K[len(S_350K)-2])/1.5

for i in range(1,len(S_350K)-1):
    S_350K_RM[i]=(0.5*S_350K[i-1]+S_350K[i]+0.5*S_350K[i+1])/2.

S_600K_RM=S_600K

S_600K_RM[0]=(S_600K[0]+0.5*S_600K[1])/1.5
S_600K_RM[len(S_600K)-1]=(S_600K[len(S_600K)-1]+0.5*S_600K[len(S_600K)-2])/1.5

for i in range(1,len(S_600K)-1):
    S_600K_RM[i]=(0.5*S_600K[i-1]+S_600K[i]+0.5*S_600K[i+1])/2.


#%% FLux
fig, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True,sharex=True, figsize=(14,8),dpi=500)

b1=-300
b2=300
Colorlevels=np.linspace(b1,b2,100,endpoint=True)
#Colorlevels=[b1,b1/2,b1/5,b1/10,b1/100,0,b2/100,b2/10,b2/5,b2/2,b2]
Edges1=np.linspace(b2,100000000,2,endpoint=True)
Edges2=np.linspace(-100000000,b1,2,endpoint=True)
#norm = colors.BoundaryNorm(boundaries=Colorlevels, ncolors=256)

Timevec=np.linspace(1,179,179)/2
cs1=ax1.contourf(Lat,Timevec,Flux_600K,levels=Colorlevels,cmap=cm.seismic)
cs1=ax1.contourf(Lat,Timevec,Flux_600K,levels=Edges1,colors='DarkRed')
cs1=ax1.contourf(Lat,Timevec,Flux_600K,levels=Edges2,colors='DarkBlue')
CS=ax1.contour(Lat,Timevec,Flux_600K,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.tick_params(axis='both', which='minor', labelsize=20)
ax1.set_ylabel('Time in days', fontsize=20)

Timevec=np.linspace(1,179,179)/2
cs2=ax2.contourf(Lat,Timevec,Flux_600K,levels=Colorlevels,cmap=cm.seismic)
cs2=ax2.contourf(Lat,Timevec,Flux_600K,levels=Edges1,colors='DarkRed')
cs2=ax2.contourf(Lat,Timevec,Flux_600K,levels=Edges2,colors='DarkBlue')
CS=ax2.contour(Lat,Timevec,Flux_600K,levels=[-1000,0,1000],linewidth=3.0,colors='k')

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


Timevec=np.linspace(1,180,180)/2
cs1=ax1.contourf(Lat,Timevec,np.array(S_mean_315_2010)/np.mean(S_mean_315_2010),levels=Colorlevels,cmap=cm.coolwarm)
CS=ax1.contour(Lat,Timevec,S_mean_315_2010,levels=[1,10,50,100,150],linewidth=3.0,colors='k')
plt.clabel(CS, fontsize=13, inline=1,fmt='%1.0f')

ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.tick_params(axis='both', which='minor', labelsize=20)
ax1.set_ylabel('Time in days', fontsize=20)

Timevec=np.linspace(1,180,180)/2
cs2=ax2.contourf(Lat,Timevec,np.array(S_mean_350_2010)/np.mean(S_mean_350_2010),levels=Colorlevels,cmap=cm.coolwarm)
cs2=ax2.contourf(Lat,Timevec,np.array(S_mean_350_2010)/np.mean(S_mean_350_2010),levels=Edges1,colors='DarkRed')
cs2=ax2.contourf(Lat,Timevec,np.array(S_mean_350_2010)/np.mean(S_mean_350_2010),levels=Edges2,colors='DarkBlue')
CS=ax2.contour(Lat,Timevec,S_mean_350_2010,levels=[1,25,50,75],linewidth=3.0,colors='k')
plt.clabel(CS, fontsize=13, inline=1,fmt='%1.0f')

ax2.tick_params(axis='both', which='major', labelsize=20)
ax2.set_xlabel('Latitude', fontsize=20)

Timevec=np.linspace(1,180,179)/2
cs3=ax3.contourf(Lat,Timevec,np.array(S_mean_600_2010)/np.mean(S_mean_600_2010),levels=Colorlevels,cmap=cm.coolwarm)
CS=ax3.contour(Lat,Timevec,np.array(S_mean_600_2010),levels=[1.5,2],linewidth=3.0,colors='k')
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


Timevec=np.linspace(1,180,180)/2
cs1=ax1.contourf(Lat,Timevec,V_mean_315_2010,levels=Colorlevels)
CS=ax1.contour(Lat,Timevec,V_mean_315_2010,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.tick_params(axis='both', which='minor', labelsize=20)
ax1.set_ylabel('Time [days]', fontsize=20)

Timevec=np.linspace(1,180,180)/2
cs2=ax2.contourf(Lat,Timevec,V_mean_350_2010,levels=Colorlevels)
cs2=ax2.contourf(Lat,Timevec,V_mean_350_2010,levels=Edges1,colors='DarkRed')
cs2=ax2.contourf(Lat,Timevec,V_mean_350_2010,levels=Edges2,colors='DarkBlue')
CS=ax2.contour(Lat,Timevec,V_mean_350_2010,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax2.tick_params(axis='both', which='major', labelsize=20)
ax2.set_xlabel('Latitude', fontsize=20)

Timevec=np.linspace(1,179,179)/2
cs3=ax3.contourf(Lat,Timevec,V_mean_600_2010,levels=Colorlevels)
CS=ax3.contour(Lat,Timevec,V_mean_600_2010,levels=[-1000,0,1000],linewidth=3.0,colors='k')

ax3.tick_params(axis='both', which='major',labelsize=20)

ax3.set_xticks([0,30,60,90])

cax = fig.add_axes([0.12, -0.02, 0.79, 0.05])
cbar=fig.colorbar(cs3, cax=cax,orientation='horizontal',ticks=[-3,-2,-1,0,1,2,3,4,5])
cbar.ax.tick_params(labelsize=15) 
cbar.ax.set_xlabel('Meridional Velocity [m/s]',fontsize=20) 
