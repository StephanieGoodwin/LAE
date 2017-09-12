import numpy as np 
import matplotlib.pyplot as plt

def initialBell(x):
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi),2),0)

nx =100
c=0.2

#loop over remaining time-steps 9nt0 using CTCS
nt =2000

#derived quanties 

u = 1.
dx = 1./nx
dt = c*dx/u
t = nt*dt

x=np.linspace(0.0,1.0,nx+1)
phi =initialBell(x)
phiNew = phi.copy()
phiOld = phi.copy()

K =0.001*dt/(dx**2)

#FTCS for the first time-step

#loop over space
for j in xrange (1, nx):
    phi[j] = phiOld[j] + K*(phiOld[j+1] - 2*phiOld[j] + phiOld[j-1])  #change

#apply periodic boundary conditions
phi[0] = phiOld[0] + K*(phiOld[1] - 2*phiOld[0] + phiOld[nx-1]) #change
phi[nx] = phi[0]

for n in xrange(1,nt):
    for j in xrange(1, nx):
        phiNew[j] = phi[j] + K*(phi[j+1] - 2*phi[j] + phi[j-1])  #change
    phiNew[0] = phi[0] + K*(phi[0+1] - 2*phi[0] + phi[nx-1])
    phiNew[nx] = 0
    #phiNew[0] = phiOld[0] - 2*K*(phi[j+1] - 2*phi[0] + phi[nx-1])  #change 
    #phiNew[nx] = phiNew[0]

    phiOld =phi.copy()
    phi = phiNew.copy()

print (x)
print (u)
print(initialBell(x - u*t))

#plot the solution in comparison to the analytic solution
plt.plot(x, initialBell(x), 'k', label = 'analytic')
plt.plot(x, phi, 'b', label='FTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle=':', color='black')
plt.savefig('Increased_time_step')
plt.show()







 
