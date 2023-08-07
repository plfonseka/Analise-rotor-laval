# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

EDO Solver - Variação das Órbitas
"""
import numpy as np

def vib(t,z):
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
    wn = 300#np.sqrt(ke/m)
    
    #wn = 110,wn,150,300
    
    g = np.zeros((4))
    
    g[0] = z[2]
    g[1] = z[3]
    g[2] = (1/m*(-c*z[2]-ke*z[0]+me*(wn**2)*np.cos(wn*t)))
    g[3] = (1/m*(-c*z[3]-ke*z[1]+me*(wn**2)*np.sin(wn*t)-P))
    
    return g
