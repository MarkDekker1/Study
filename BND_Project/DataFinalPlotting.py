Flux600=Fluxmean


fig=plt.figure(num=None, figsize=(10,8),dpi=150, facecolor='w', edgecolor='k')
Timevec=np.linspace(1,179,179)/2

#f, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True,sharex=True, figsize=(15,8))
ax = fig.add_subplot(111)    # The big subplot
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

ax.set_xlabel('Latitude', fontsize=14)
ax.set_ylabel('Time in days', fontsize=14)

#%%


f, (ax1, ax2, ax3) = plt.subplots(1,3,sharey=True,sharex=True, figsize=(10,8))

Colorlevels=np.linspace(,12,12,endpoint=True)

cs=ax1.contourf(Lat,Timevec,Fluxmatrix,25)
CS=ax1.contour(Lat,Timevec,Fluxmatrix,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#plt.clabel(CS, fontsize=9, inline=1,fmt='%1.0f')
ax1.tick_params(axis='both', which='major', labelsize=14)
ax1.tick_params(axis='both', which='minor', labelsize=14)
ax1.set_ylabel('Time in days', fontsize=14)
#cbar=ax1.colorbar(cs)
#cbar.ax.tick_params(labelsize=15) 

#plt.subplots(1,2,sharey=True)
cs=ax2.contourf(Lat,Timevec,Fluxmatrix,25)
CS=ax2.contour(Lat,Timevec,Fluxmatrix,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#plt.clabel(CS, fontsize=9, inline=1,fmt='%1.0f')
ax2.tick_params(axis='both', which='major', labelsize=14)
ax2.set_xlabel('Latitude', fontsize=14)
#cbar=ax2.colorbar(cs)
#cbar.ax.tick_params(labelsize=15)

#plt.subplots(1,3,sharey=True)
cs=ax3.contourf(Lat,Timevec,Fluxmatrix,25)
CS=ax3.contour(Lat,Timevec,Fluxmatrix,levels=[-1000,0,1000],linewidth=3.0,colors='k')
#plt.clabel(CS, fontsize=9, inline=1,fmt='%1.0f')
ax3.tick_params(axis='both', which='major', labelsize=14)
#cbar=ax3.colorbar(cs)
#cbar.ax.tick_params(labelsize=15) 
plt.colorbar(cs)