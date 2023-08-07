# -*- coding: utf-8 -*-
"""
Universidade Estadual de Campinas
IM 342 - Análise de Máquinas Rotativas
Pedro Lucas - Ra 263117

EDO Solver - Deslocamento Lateral
"""
import numpy as np

def vib(t,z):
  
    gv = 9.8
    de = 12E-3
    dd = 100E-3
    le = 850E-3
    me = 1.5E-3
    m = 0.925
    e = me/m
    E = 200E9
    I = np.pi*(de**4)/64
    ke = 48*E*I/le**3
    c = ke*1E-3
    P = m*gv
    jg = m/2*((dd/2)**2)
    Tr = 0.280
    
    # Torque aplicado ao conjunto
    # To = 0.300;% Torque aplicado no Eixo
    # 0.280 não passa a zona de ressonância
    # 0.300 passa lentamente a zona de ressonância
    # 0.750 passa rapidamente a zona de ressonância
    
    A = 1/jg*(Tr-e*c*z[3]*np.sin(z[2])+e*c*z[4]*np.cos(z[2])-ke*e*z[0]*np.sin(z[2])+ke*e*z[1]*np.cos(z[2]))
    
    g = np.zeros((6))
    
    g[0] = z[3]
    g[1] = z[4]
    g[2] = z[5]
    g[3] = (1/m*(-c*z[3]-ke*z[0]+me*(A*np.sin(z[2])+((z[5])**2)*np.cos(z[2]))))
    g[4] = (1/m*(-P-c*z[4]-ke*z[1]+me*(-A*np.cos(z[2])+((z[5])**2)*np.sin(z[2]))))
    g[5] = A
    
    return g
