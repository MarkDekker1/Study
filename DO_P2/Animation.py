#Preambule
#   TYPE %matplotlib qt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import ma

ax, fig = plt.figure(num = 0, figsize = (12, 8))

xvec=[0,1,2]
yvec=[0,1,2]

plt.xlim([0,2])
plt.ylim([0,2])
plt.xlabel('Zonal distance',fontsize=13)
plt.ylabel('Meridional distance',fontsize=13)
ax.set_title('Model Horizontal Field')
ax01.set_title('Radiation')
ax01.set_ylim(-750,1000)
ax01.set_xlim(0,100)


#############
np.seterr(over='raise')

mx=100
mt=500
dx=1./mx
dt=10000
tmax=500000.
L=1.

r=0.1
Lambda=0.


Cw0=1./(dt*dx**2)-1./(4.*dx)+r/(2.*dx**2)
Cc0=-(2./(dt*dx**2)+(Lambda+1)/dt+r/(dx**2)+r/2.)
Ce0=1./(dt*dx**2)+1./(4.*dx)+r/(2.*dx**2)

#def hf(phim1,phi1,phip1):
#    return ((phip1-2.*phi1+phim1)/(dt*dx**2)+(Lambda+1)*phi1/dt-(phip1-phim1)/(4.*dx)-r*((phip1-2*phi1+phim1)/(2*dx**2)-phi1/2.)+1.)

def hf(phim1,phi1,phip1):
    return (phip1-2*phi1+phim1)/(dt*dx**2)+(Lambda+1)*phi1/dt-(phip1-phim1)/(4*dx)-r*((phip1-2*phi1+phim1)/(2*dx**2)-phi1/2.)+1.
    

n=mx
tt=int(tmax/dt)
#b0=Cc0*np.ones(n)
h=np.zeros(n)
phin=np.zeros(n)
phip=np.zeros(shape=(tt,n))



# Data Placeholders
yp1=np.zeros(0)

xvec,yvec=np.meshgrid(xvec,yvec)

#Radiation plot
LIJN1, = ax01.plot(t,yp1,'b-', label="QS")

#Timeloop
def plotter(vec):
    return np.array(np.transpose([vec[0:3],vec[3:6],vec[6:9]]))
    
def init():
    imobj.set_data(Ta)
    time_text.set_text('time = 0.0')

    return imobj , time_text
    
def animate(self):
    global data
    global LIJN1
    global t
    global x
    global yp1
    global qk
    
    yp1=np.append(yp1,np.mean(QS))
    yp2=np.append(yp2,np.mean(QL))
    yp3=np.append(yp3,np.mean(QE))
    yp4=np.append(yp4,np.mean(QG))
    yp5=np.append(yp5,np.mean(QH))
    yp6=np.append(yp6,np.mean(Ta))
    yp7=np.append(yp7,np.mean(Ts))
    yp8=np.append(yp8,np.mean(Evec))
    yp9=np.append(yp9,np.mean(Ta2))
    t=np.append(t,x)

    x += 1.0    
    
    LIJN1.set_data(t,yp1)
    LIJN2.set_data(t,yp2)
    LIJN3.set_data(t,yp3)
    LIJN4.set_data(t,yp4)
    LIJN5.set_data(t,yp5)
    LIJN6.set_data(t,yp6)
    LIJN7.set_data(t,yp7)
    LIJN8.set_data(t,yp8)
    LIJN9.set_data(t,yp9)
    
    time_text.set_text('time = %.1f' % self )
    SB_text.set_text('SB = %.1f' % np.mean(Evec) )
    AB_text.set_text('AB = %.1f' % np.mean(Avec) )
    AB2_text.set_text('A2B = %.1f' % np.mean(Avec2) )
    new=plotter(Ts)
    imobj.set_data(new)
       
    imobj.set_zorder(0)
    Quivers.set_UVC(plotter(U),plotter(V))
    
    ax1=plt.axhline(xmin=0,xmax=1,y=0,linewidth=3,color='k')
    ax2=plt.axvline(ymin=0,ymax=1,x=0,linewidth=3,color='k')
    ax3=plt.axhline(xmin=0,xmax=1,y=2,linewidth=3,color='k')
    ax4=plt.axvline(ymin=0,ymax=1,x=2,linewidth=3,color='k')
    ax5=plt.axvline(ymin=0,ymax=1,x=0.5,linewidth=3,color='k',ls='--')
    #hoi=plt.contour([0,1,2],[0,1,2],plotter(Ta),15,animated=True)
    
    
    if x >= 0.:
        LIJN1.axes.set_xlim(x-100.+1.0,x+1.0)
        LIJN2.axes.set_xlim(x-100.+1.0,x+1.0)
        LIJN3.axes.set_xlim(x-100.+1.0,x+1.0)
        LIJN4.axes.set_xlim(x-100.+1.0,x+1.0)
        LIJN5.axes.set_xlim(x-100.+1.0,x+1.0)
        LIJN6.axes.set_xlim(x-100.+1.0,x+1.0)
        LIJN7.axes.set_xlim(x-100.+1.0,x+1.0)
        LIJN8.axes.set_xlim(x-100.+1.0,x+1.0)
        LIJN9.axes.set_xlim(x-100.+1.0,x+1.0)
    
    qk = plt.quiverkey(Quivers, 0.1, 0.7, 2, r'$2 \frac{m}{s}$', labelpos='W',
                       fontproperties={'weight': 'bold'})
    
    return imobj , Quivers,time_text,ax1,ax2,ax3,ax4,ax5,SB_text,AB_text,AB2_text,LIJN1,LIJN2,LIJN3,LIJN4,LIJN5,LIJN6,LIJN7,LIJN8,LIJN9,qk


def forceAspect(ax,aspect=1):
    im = ax.get_images()
    extent =  im[0].get_extent()
    ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)

data = list(Ts)
#imobj = plt.contourf(xvec,yvec,plotter(data),animated=True,aspect=0.5,extent=[0, 2.0, 0.0, 2.0], alpha=1.0, zorder=1)
imobj=plt.imshow(plotter(data), cmap='jet', animated=True,aspect=0.5,extent=[0, 2.0, 0.0, 2.0], alpha=1.0, zorder=1)
plt.colorbar(orientation='horizontal')
plt.clim(240,310)
X,Y=np.meshgrid([0,1,2],[2,1,0])
Quivers=plt.quiver(plotter(U),plotter(V),units='inches')
qk = plt.quiverkey(Quivers, 0.1, 0.7, 2, r'$2 \frac{m}{s}$', labelpos='W',
                   fontproperties={'weight': 'bold'})

l, r, b, top = plt.axis()
dx, dy = r - l, top - b
plt.axis([l - 0.05*dx, r + 0.05*dx, b - 0.05*dy, top + 0.05*dy])

line_simu, = plt.plot([], [],"r--", lw=2, markersize=4 , label = "Some curve" ,  zorder= 1 )
time_text = plt.text(0.1, 0.1, '', zorder=10)
SB_text = plt.text(0.1, 1.9, '', zorder=10)
AB_text = plt.text(0.1, 1.8, '', zorder=10)
AB2_text = plt.text(0.1, 1.7, '', zorder=10)

anim = animation.FuncAnimation(fig, animate,  frames=range(1000), interval=200,blit=True,repeat=False)