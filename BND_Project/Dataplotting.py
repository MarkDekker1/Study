#Preambule
import numpy as np
import matplotlib.pyplot as plt

#%%

fig, ax1 = plt.subplots()
ax1.plot(Lat,Fluxmean)
ax1.plot(Lat,Smean, 'b--')
ax1.set_xlabel('Latitude')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('Isentropic mass flux; isentropic density', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')


ax2 = ax1.twinx()
ax2.plot(Lat,Vmean, 'r')
ax2.set_ylabel('Meridional velocity [m/s]', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.show()
#plt.legend(['Flux','V [cm/s]','S'])

#%% Hov moller zonal means Flux
plt.figure(num=None, figsize=(6,8),dpi=150, facecolor='w', edgecolor='k')
Timevec=np.linspace(1,180,180)/2
cs=plt.contourf(Lat,Timevec,Fluxmatrix,25)
CS=plt.contour(Lat,Timevec,Fluxmatrix,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#plt.clabel(CS, fontsize=9, inline=1,fmt='%1.0f')
plt.title('Isentropic Mass Flux (mean part)')
plt.xlabel('Latitude',fontsize=13)
plt.ylabel('Time (days)',fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)
cbar=plt.colorbar(cs)
cbar.ax.tick_params(labelsize=15) 
#%% Hov moller zonal means Sigma
plt.figure(num=None, figsize=(6,8),dpi=150, facecolor='w', edgecolor='k')
Timevec=np.linspace(1,180,180)/2
cs=plt.contourf(Lat,Timevec,Smatrix,25)
#CS=plt.contour(Lat,Timevec,Smatrix,levels=[0,50,100,150],linewidth=3.0,colors='k')
#plt.clabel(CS, fontsize=9, inline=1,fmt='%1.0f')
plt.title('Isentropic Density')
plt.xlabel('Latitude',fontsize=13)
plt.ylabel('Time (days)',fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)
cbar=plt.colorbar(cs)
cbar.ax.tick_params(labelsize=15) 
#%% Hov moller zonal means V
plt.figure(num=None, figsize=(6,8),dpi=150, facecolor='w', edgecolor='k')
Timevec=np.linspace(1,180,180)/2
cs=plt.contourf(Lat,Timevec,Vmatrix,25)
CS=plt.contour(Lat,Timevec,Vmatrix,levels=[-20,-10,0,10,20],linewidth=3.0,colors='k')
#plt.clabel(CS, fontsize=9, inline=1,fmt='%1.1f')
#plt.title('Meridional velocity')
plt.xlabel('Latitude',fontsize=13)
plt.ylabel('Time (days)',fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.tick_params(axis='both', which='minor', labelsize=14)
cbar=plt.colorbar(cs)
cbar.ax.tick_params(labelsize=15) 