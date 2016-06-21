import numpy as np
import matplotlib.pyplot as plt

PulseV=np.zeros(len(Vmatrix))
PulseS=np.zeros(len(Smatrix))

for i in range(0,len(Vmatrix)):
    PulseV[i]=np.mean(Vmatrix[i][0:30])
    PulseS[i]=np.mean(Smatrix[i][0:30])