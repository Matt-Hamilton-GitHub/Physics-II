import math

N=1E4 #number of particles
m=5.33E-26 #mass of particle
kb=1.38E-23 #Boltzmann constant
T=500 #temperture in K


def Nv(v):
  return 4*math.pi*N*(m/(2*math.pi*kb*T))**(3/2)*(v**2*math.exp(-m*(v**2)/(2*kb*T)))



Nv(0.02)


# graphing functions
import matplotlib.pyplot as plt
import numpy as np

v=np.linspace(0, 1500,150 )
f_v = np.vectorize(lambda v: Nv(v)) 
y=f_v(v)
plt.plot(v, y, label='Number Density Plot')
plt.xlabel("v (m/s)")
plt.ylabel("Maxwell-Boltzmann Distribution")
plt.legend()
plt.show()


vmp=(2*kb*T/m)**0.5
print(vmp)