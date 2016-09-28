# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import math as mt
import  PotEneGenSqu

#the main program of Langevin Dynamics
#input parameters format(in the first line of the input.txt file): 
#x0: initial position
#v0: initial velocity
#T: temperature
#damp: dampling coefficient
#delta_t: time step
#Time: total time
#m


####### the force parameter
#F: net force
#Fd: Drage force
#Fs: solvent force
#Fp: potential force


class Langevin_dynamics():
    def __init__(self):
        pass

    def tran_input_float(self, file_name):
        intxt =  open(file_name, 'r')
        for line in intxt: 
            input_stri = line.split()
        intxt.close()
        input_int = list(map(float, input_stri))
        return input_int
     	
    def dynamics(self, X0, V0, T, damp, delta_t, Time, m, L, X_pot, Fp, Tg):    # the evolution
        mean = 0
        std = mt.sqrt(2 * mt.sqrt(damp) * T )
        x = X0
        v = V0
        fp =  Fp[0]
        V = np.zeros(Tg)
        X = np.zeros(Tg)
        t_arr = np.linspace(0, Time, Tg)
        Fs = rd.gauss(mean, std)
        a = ( -damp * v  + Fs - fp ) / m
        for t in range(Tg):
            v = v + 0.5 * a * delta_t
            X[t] = x + delta_t * v
            X[t] = X[t] % L
            x = round(X[t], 3)      # the boundary condition; only keep the first four digits after the decimal
            itemindex = np.where(X_pot == x)[0][0]
            fp = Fp[itemindex]      # find the force corresponding to the current position
            Fs = rd.gauss(mean, std)     # using gaussian distribution to generate the solvent force
            a = ( -damp * v + Fs - fp ) / m
            V[t] = v + 0.5 * a * delta_t
            v = V[t]
        return t_arr, X, V

    def output_f_v(self, file_name, Tg, t_arr, X, V):  # output the file with force and position at every time
        with open(file_name, 'w') as f:
            f.write('#this format is:\n')
            f.write('#index t X V\n')
            for index in range(Tg):
                f.write('%s %10s %10s %10s\n' %(index + 1, t_arr[index], X[index], V[index]))

