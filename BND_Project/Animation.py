import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#%% Which do we plot?
A_1=RefM_315_2010
A_2=Flux_eddy315_10

B_1=np.zeros(91)
B_2=np.zeros(91)

for i in range(0,91):
    B_1[i]=np.mean(A_1[:,i])
    B_2[i]=np.mean(A_2[:,i])

#%% Sharply smoothen in t-direction:
A=A_1
A_RM=A

A_RM[0]=(A[0]+0.5*A[1])/1.5
A_RM[len(A)-1]=(A[len(A)-1]+0.5*A[len(A)-2])/1.5

for i in range(1,len(A)-1):
    A_RM[i]=(0.5*A[i-1]+A[i]+0.5*A[i+1])/2.

#%%#Preambule

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 90), ylim=(-200, 200))
#line, = ax.plot([], [], lw=2)
Lat=np.linspace(0,90,91,endpoint=True)
Lat=Lat[::-1]


y_m=np.zeros(91)
y_e=np.zeros(91)


line_1, = ax.plot([],[],'b-',linewidth=3)
line_2, = ax.plot([],[],'r-',linewidth=3)

line_3, = ax.plot(Lat,B_1,'b--',linewidth=1)
line_4, = ax.plot(Lat,B_2,'r--',linewidth=1)
line_6, = ax.plot([],[],'r.',linewidth=3)
line_7, = ax.plot([],[],'b.',linewidth=3)

ax.legend([line_1,line_2,line_3,line_4],['[v][s]','[v*s*]','temporal mean [v][s]','temporal mean[v*s*]'], bbox_to_anchor=(0., 1.02, 1., .102), loc=2,
           ncol=5, mode="expand", borderaxespad=3.,fontsize=25,prop={'size':10})

plt.plot((0,90), (0,0), 'k-',linewidth=1)

plt.xlabel('Latitude',fontsize=20)
plt.ylabel('Isentropic Mass flux',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
line_5 = plt.scatter([1],[1], alpha=0.5,s=150)
colors=np.linspace(0,len(Lat),len(Lat))

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(t):
    global line_1
    global line_2
    global line_5
    
    global line_6
    global line_7
    
    #phip[t]=phi   
    
    y_m = A_1[t]
    y_e = A_2[t]
    #y = np.sin(2 * np.pi * (x - 0.01 * i)) 
    
    line_1.set_data(Lat, y_m)
    line_2.set_data(Lat, y_e)
    line_6.set_data(Lat[0:30], np.zeros(30)+np.mean(y_e[0:30]))
    line_7.set_data(Lat[0:30], np.zeros(30)+np.mean(y_m[0:30]))
    
    line_5=plt.scatter([1],[1], c=colors[t],alpha=0.5,s=150)
    #line_5.set_edgecolors(colors1[t])
    
    time_text.set_text('Day %.1f' % t )
    return line_1,line_2,line_5,line_6,line_7,time_text


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=range(len(Lat)), interval=300,blit=True,repeat=True)
time_text = plt.text(0.8, 180, '', zorder=10)
plt.show()