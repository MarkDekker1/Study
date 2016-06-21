import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#Preambule
np.seterr(over='raise')
mx=100
mt=500
dx=1./mx
dt=1000
tmax=1.
L=1.
r=0.1
Lambda=0.
Cw0=1./(dt*dx**2)-1./(4.*dx)+r/(2.*dx**2)
Cc0=-(2./(dt*dx**2)+(Lambda+1)/dt+r/(dx**2)+r/2.)
Ce0=1./(dt*dx**2)+1./(4.*dx)+r/(2.*dx**2)

def hf(phim1,phi1,phip1):
    return (phip1-2*phi1+phim1)/(dt*dx**2)+(Lambda+1)*phi1/dt-(phip1-phim1)/(4*dx)-r*((phip1-2*phi1+phim1)/(2*dx**2)-phi1/2.)+1.
n=mx
tt=int(tmax/dt)
h=np.zeros(n)
phin=np.zeros(n)
phip=np.zeros(shape=(tt,n))
b=np.zeros(n)
phi=np.zeros(n)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-1, 0.2))
line, = ax.plot([], [], lw=2)
xax=np.linspace(0.,1.,mx)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(t):
    global phin
    global phi
    global h
    global b
    
    h[0]=hf(0.,phi[0],phi[1])
    for k in range(1,n-1):
        h[k]=hf(phi[k-1],phi[k],phi[k+1])
    h[n-1]=hf(phi[n-2],phi[n-1],0.)
    
    for i in range(0,n):
        b[i]=Cc0
    for k in range(1,n):
        m=Cw0/b[k-1]
        b[k]=b[k]-m*Ce0
        h[k]=h[k]-m*h[k-1]
        
    phin[n-1]=h[n-1]/b[n-1]
    for k in range(n-2,0,-1):
        phin[k]=(h[k]-Ce0*phin[k+1])/b[k]
    phi=phin
    
    #phip[t]=phi   
    
    y = np.sin(2 * np.pi * (xax - 0.01 * t))
    #y = np.sin(2 * np.pi * (x - 0.01 * i)) 
    
    line.set_data(xax, phin)
    time_text.set_text('time = %.1f' % t )
    return line,time_text


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=range(1000), interval=50,blit=True,repeat=False)
time_text = plt.text(0.8, 0., '', zorder=10)
plt.show()