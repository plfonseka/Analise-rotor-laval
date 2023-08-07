# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

Resposta Temporal do Sistema - Deslocamento Lateral
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp 
from vib_rotor import vib

x0 = np.array([[0],[0],[0]])
xp0 = np.array([[0],[0],[0]])
aux = np.block([[x0],[xp0]])
z0 = np.reshape(aux,(len(aux),))

tin = 0
tf = 3

sol = solve_ivp(vib,[tin,tf],z0);

T = sol.t
Z = sol.y

dof = len(x0)
x = Z[0:dof,:]
xp = Z[dof:2*dof,:]

############ PLOT Uy #############
fig1, ax1 = plt.subplots()
ax1.set_xlabel('tempo [s]')
ax1.set_ylabel('Deslocamento [m]')
ax1.plot(T,x[0,:], 'b')

ax2 = ax1.twinx()
ax2.set_ylabel('Velocidade de rotação [rad/s]')
ax2.plot(T,xp[2,:], 'k--')

ax1.margins(x=0.0)
#plt.show()
# plt.savefig('uy_insuficiente.png',dpi=600)

########### PLOT Uz ##############
fig2, ax1 = plt.subplots()
ax1.set_xlabel('tempo [s]')
ax1.set_ylabel('Deslocamento [m]')
ax1.plot(T,x[1,:], 'b')

ax2 = ax1.twinx()
ax2.set_ylabel('Velocidade de rotação [rad/s]')
ax2.plot(T,xp[2,:], 'k--')

ax1.margins(x=0.0)
#plt.show()
# plt.savefig('uz_insuficiente.png',dpi=600)

    


