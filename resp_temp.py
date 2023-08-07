# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

Resposta Temporal do Sistema - Variação das Órbitas
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp 
from vib import vib

gv = 9.8
de = 12E-3
le = 850E-3
me = 1.5E-3
m = 0.925
E = 200E9
I = np.pi*(de**4)/64
ke = 48*E*I/le**3
c = ke*1E-3
P = m*gv
e = me/m
w = 300#np.sqrt(ke/m)

x0 = np.array([[0],[0]])
xp0 = np.array([[0],[0]])
aux = np.block([[x0],[xp0]])
y0 = np.reshape(aux,(len(aux),))

tin = 0
tf = 2

sol = solve_ivp(vib,[tin,tf],y0);

T = sol.t
Y = sol.y

l=150
dof = len(x0)
x = Y[0:dof,l:]
xp = Y[dof:2*dof,l:]

plt.plot(x[0,:]+e*np.cos(w*T[l:,]),x[1,:]+e*np.sin(w*T[l:,]),'r',label='G')
plt.plot(x[0,:],x[1,:],'b',label='W')
plt.axis('equal')
plt.legend(loc='upper right')
plt.xlabel('Uy')
plt.ylabel('Uz')
plt.title('Variação das Órbitas W e G')

#plt.savefig('orbita_max_wn.png',dpi=600)

    


