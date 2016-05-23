#Modules
import numpy as np
import matplotlib.pyplot as plt

#Preambule
C=5e7
alpha=0.3
e=0.0
obliquity=23.45
sigmam=0.3
qm=400e-6
g=9.81
sigmaB=5.67e-8
S=1366.
dm=1.495978707e9
phi=67.
kappa=0.286
pref=1e5

#Functions
def delta(p):
	return sigmam*qm*p/g

def d(t):
	return dm*(1+e*np.sin((2.*np.pi/365.)*(272.+t)))

def declination(t):
	return (np.pi*obliquity/180.)*np.sin((2.*np.pi/365.)*(285+t))
	
def DH(t):
	return np.arccos(-np.tan(phi*2.*np.pi/360.)*np.tan(declination(t)))
	
def Q(t):
	return (1.-alpha)*S/np.pi*(dm/d(t))**2.*(DH(t)*np.sin(phi*2.*np.pi/360.)*np.sin(declination(t))+np.cos(phi*2.*np.pi/360.)*np.cos(declination(t))*np.sin(DH(t)))
	
def Theta(p,t):
	return (Q(t)*(1+delta(p))/(2*sigmaB))**(0.25)*(pref/p)**(kappa)

def idensity(p,t):
	return 1./g*(2.*sigmaB/Q(t))**(0.25)*(p/pref)**kappa*p*(delta(p)+1.)**(0.75)*(kappa*(1.+delta(p))-delta(p)/4)**(-1)

#Plots
March20=31+28+20
June20= 31+28+31+30+31+20
Sept20= 31+28+31+30+31+30+31+31+20
Dec20=  31+28+31+30+31+30+31+31+30+31+30+20

plt.figure(num=None, figsize=(6,6),dpi=150, facecolor='w', edgecolor='k')

for j in [March20,June20,Sept20,Dec20]:
	t=j
	Tvec=np.zeros(700)
	Dvec=np.zeros(700)
	for i in range(0,700):
		p=10**(2.5)+i*1e3
		Tvec[i]=Theta(p,t)
		Dvec[i]=idensity(p,t)
	plt.plot(Dvec,Tvec,linewidth=3)

plt.xlabel('Isentropic density [$kg$ $m^{-2}$ $K^{-1}$]',fontsize=18)
plt.ylabel('Potential temperature [$K$]',fontsize=18)
plt.ylim([0,1000])
plt.xlim([0,150])
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.legend(['March 20th','June 20th','September 20th','December 20th'])
plt.axhline(y=315, xmin=0, xmax=150, hold=None,color='lightgrey',linewidth=3)
plt.axhline(y=370, xmin=0, xmax=150, hold=None,color='lightgrey',linewidth=3)
