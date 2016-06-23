# Refine mean parts:
RefM_315_2010=Flux_mean_315_2010[0:179:2]
RefM_350_2010=Flux_mean_350_2010[0:179:2]
RefM_315_2007=Flux_mean_315_2007[0:179:2]
RefM_600_2007=Flux_mean_600_2007[0:179:2]
RefM_600_2010=Flux_mean_600_2010[0:179:2]
#RefM_600_2007=Flux_mean_600_2007[0:179:10]

Vec315M_P_10=[]
Vec315M_S_10=[]
Vec350M_P_10=[]
Vec350M_S_10=[]

Vec315M_P_07=[]
Vec315M_S_07=[]
Vec350M_P_07=[]
Vec350M_S_07=[]

Vec315E_P_10=[]
Vec315E_S_10=[]
Vec350E_P_10=[]
Vec350E_S_10=[]

Vec315E_P_07=[]
Vec315E_S_07=[]
Vec350E_P_07=[]
Vec350E_S_07=[]

Vec600M_P_07=[]
Vec600M_S_07=[]
Vec600E_P_07=[]
Vec600E_S_07=[]
Vec600M_P_10=[]
Vec600M_S_10=[]
Vec600E_P_10=[]
Vec600E_S_10=[]

for i in range(0,90):
     #2010
	Vec315M_S_10.append(np.mean(RefM_315_2010[i][55:65]))
	Vec350M_S_10.append(np.mean(RefM_350_2010[i][55:65]))
	
	Vec315E_S_10.append(np.mean(Flux_eddy315_10[i][55:65]))
	Vec350E_S_10.append(np.mean(Flux_eddy350_10[i][55:65]))
	
	Vec315M_P_10.append(np.mean(RefM_315_2010[i][0:30]))
	Vec350M_P_10.append(np.mean(RefM_350_2010[i][0:30]))
	
	Vec315E_P_10.append(np.mean(Flux_eddy315_10[i][0:30]))
	Vec350E_P_10.append(np.mean(Flux_eddy350_10[i][0:30]))
      
	Vec315E_P_07.append(np.mean(Flux_eddy315_07[i][0:30]))
	Vec315E_S_07.append(np.mean(Flux_eddy315_07[i][55:65]))
      
	Vec315M_P_07.append(np.mean(RefM_315_2007[i][0:30]))
	Vec315M_S_07.append(np.mean(RefM_315_2007[i][55:65]))
 
	Vec600M_S_07.append(np.mean(RefM_600_2007[i][55:65]))
	Vec600M_P_07.append(np.mean(RefM_600_2007[i][0:30]))
	Vec600E_S_07.append(np.mean(Flux_eddy600_07[i][55:65]))
	Vec600E_P_07.append(np.mean(Flux_eddy600_07[i][0:30]))
 
	Vec600M_S_10.append(np.mean(RefM_600_2010[i][55:65]))
	Vec600M_P_10.append(np.mean(RefM_600_2010[i][0:30]))
	Vec600E_S_10.append(np.mean(Flux_eddy600_10[i][55:65]))
	Vec600E_P_10.append(np.mean(Flux_eddy600_10[i][0:30]))

#%%


	
#%%
	
C_1=Vec600M_P_10
C_2=Vec600E_P_10
Phasedif=0
C_3=[]
for i in range(0,len(C_1)-Phasedif):
    C_3.append(C_1[i+Phasedif])

C_4=C_2[0:len(C_3)]
colors=np.linspace(0,len(C_3),len(C_3))
YLIM=[-100,50]
XLIM=[-100,200]
	
plt.figure(num=None, figsize=(5,5),dpi=150, facecolor='w', edgecolor='k')
plt.scatter(C_3,C_4, c=colors, alpha=0.5,s=150)
#plt.plot((0, 0), (YLIM[0],YLIM[1]), 'k-',linewidth=1)
#plt.plot((XLIM[0],XLIM[1]), (0, 0), 'k-',linewidth=1)
#plt.xlim(XLIM)
#plt.ylim(YLIM)
plt.xlabel('[v*s*]',fontsize=20)
plt.ylabel('[v][s]',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)

#%%
def acf(x, length=20):
    return np.array([1]+[np.corrcoef(x[:-i], x[i:]) \
        for i in range(1, length)])
            
def autocorr(x, t=1):
    np.corrcoef(np.array([x[0:len(x)-t], x[t:len(x)]]))