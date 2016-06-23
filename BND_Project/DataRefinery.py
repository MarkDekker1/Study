Flux_mean_600_2010=np.array(Flux_mean600)
Flux_eddy_315_2007=np.array(Flux_eddy315)
Flux_eddy_350_2007=np.array(Flux_eddy350)
Flux_eddy_600_2007=np.array(Flux_eddy600)
V_mean_600_2010=np.array(Vd)

S_mean_600_2010=np.array(Smatrix)

#%%

Flux_mean_315_2007=np.array(Flux_315K)
Flux_mean_350_2007=np.array(Flux_350K)
Flux_mean_600_2007=np.array(Flux_600K)

V_mean_315_2007=np.array(Vmatrix)
V_mean_350_2007=np.array(Vmatrix001)
V_mean_600_2007=np.array(Vmatrix000)

S_mean_315_2007=np.array(Smatrix)
S_mean_350_2007=np.array(Smatrix001)
S_mean_600_2007=np.array(Smatrix000)


#%%
#For 2007

#Flux_315K=Fluxmatrix
#Flux_350K=Fluxmatrix001
#Flux_600K=Fluxmatrix000

V_315K=Vmatrix
V_350K=Vmatrix001
V_600K=Vmatrix000

S_315K=Smatrix
S_350K=Smatrix001
S_600K=Smatrix000


#%% For 2010:
Flux_600K=Fluxmatrix000
V_600K=Vmatrix000
S_600K=Smatrix000

#%% Eddies

Flux_eddy315_10=[]
Flux_eddy350_10=[]
Flux_eddy600_10=[]
Flux_eddy315_07=[]
Flux_eddy350_07=[]
Flux_eddy600_07=[]


for i in range(0,91):
	eddy315vec7=[]
	eddy350vec7=[]
	eddy600vec7=[]
	eddy315vec1=[]
	eddy350vec1=[]
	eddy600vec1=[]
	for j in range(0,90):
		eddy315vec7.append(np.mean(eddy315res07[i][:][j]))
		eddy350vec7.append(np.mean(eddy350res07[i][:][j]))
		eddy600vec7.append(np.mean(eddy600res07[i][:][j]))
  
		eddy315vec1.append(np.mean(eddy315_2010res[i][:][j]))
		eddy350vec1.append(np.mean(eddy350_2010res[i][:][j]))
		eddy600vec1.append(np.mean(eddy600res10[i][:][j]))
	Flux_eddy315_10.append(eddy315vec1)
	Flux_eddy350_10.append(eddy350vec1)
	Flux_eddy600_10.append(eddy600vec1)
 
	Flux_eddy315_07.append(eddy315vec7)
	Flux_eddy350_07.append(eddy350vec7)
	Flux_eddy600_07.append(eddy600vec7)

#%%
Flux_eddy315_10=np.transpose(Flux_eddy315_10)
Flux_eddy350_10=np.transpose(Flux_eddy350_10)
Flux_eddy600_10=np.transpose(Flux_eddy600_10)

Flux_eddy315_07=np.transpose(Flux_eddy315_07)
Flux_eddy350_07=np.transpose(Flux_eddy350_07)
Flux_eddy600_07=np.transpose(Flux_eddy600_07)
