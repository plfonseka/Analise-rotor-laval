# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

Parâmetros Modais do Sistema
"""
import numpy as np
import vibration_toolbox as vbt

de = 12E-3
le = 850E-3
m = 0.925
E = 200E9
I = np.pi*(de**4)/64
ke = 48*E*I/le**3
c = ke*1E-3


M = np.array([[m,0],[0,m]])
C = np.array([[c,0],[0,c]])
K = np.array([[ke,0],[0,ke]])

sys = vbt.VibeSystem(M,C,K)
