# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

Resposta em Frequência do Sistema
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt  
import vibration_toolbox as vbt

de = 12E-3
le = 850E-3
m = 0.925
E = 200E9
I = np.pi*(de**4)/64
ke = 48*E*I/le**3
c = ke*1E-3
ndof = 2

M = np.array([[m,0],[0,m]])
C = np.array([[c,0],[0,c]])
K = np.array([[ke,0],[0,ke]])

sys = vbt.VibeSystem(M,C,K)

def plot_freq_resp(self, modes=None, ax0=None, ax1=None, **kwargs):
    
    if ax0 is None or ax1 is None:
        fig, ax = plt.subplots(2)
        if ax0 is not None:
            _, ax1 = ax
        if ax1 is not None:
            ax0, _ = ax
        else:
            ax0, ax1 = ax

    omega, magdb, phase = self.freq_response(modes=modes)
    
    
    for i in range(ndof):
        ax0.plot(omega, magdb[i,i], **kwargs, color='b')
        ax1.plot(omega, phase[i,i], **kwargs, color='r')
    
    for ax in [ax0, ax1]:
        ax.set_xlim(0, max(omega))
        ax.yaxis.set_major_locator(
            mpl.ticker.MaxNLocator(prune='lower'))
        ax.yaxis.set_major_locator(
            mpl.ticker.MaxNLocator(prune='upper'))
    
    ax0.set_title('Frequência em Resposta do Sistema')
    ax0.set_ylabel('Magnitude $(dB)$')
    ax1.set_ylabel('Ângulo de Fase $(°)$')
    ax1.set_xlabel('Frequência (rad/s)')
        
    return ax0, ax1

plot_freq_resp(sys)
plt.savefig('freq_resp.png',dpi=600)



