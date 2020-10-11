# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 10:40:13 2020

@author: Vitalii

Program numerically solves the master equation for a two-level atom in external 
field by Runge-Kutta method.

"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def Eqn(t,f):
    #Equation needed to be solved
    if np.array(f).size != 2:
        f=np.array(f).reshape((2,2))
    SP=sp.matrix([[0,1],[0,0]])
    SM=SP.T
    H=5*(np.exp(1j*4*t)*SP+np.exp(-1j*4*t)*SM)
    Z=3/2*(1+0.3)*(2*SM*f*SP-SP*SM*f-f*SP*SM)+3/2*(0.3)*(2*SP*f*SM-SM*SP*f-f*SM*SP)-1j*(H*f-f*H)
    return Z.reshape((1,4))
    
def RK4(f,y0,a,b):
    #Runge-Kutta method adapted for matrix equations
    h=0.01
    i=0
    SIZE=np.array(y0).size
    y=np.zeros([int((b-a)/h)+1,SIZE],dtype=complex)
    for i in range(int((b-a)/h)+1):
        k1=f(a,y0)
        k2=f(a+h/2,y0+h/2*k1)
        k3=f(a+h/2,y0+h/2*k2)
        k4=f(a+h,y0+h*k3)
        y[i]=y0
        y0=y0+h/6*(k1+2*k2+2*k3+k4)
        a+=h
    return np.array(y) 

#Plot of the solution
plt.show(plt.plot(np.real(RK4(Eqn,np.array([1,0,0,0]),0,10))[:,:]))