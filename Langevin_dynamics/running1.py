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

import numpy as np
import random as rd
import math as mt
import  PotEneGenSqu
import Langevin_dynamics

Ld = Langevin_dynamics.Langevin_dynamics()

file_name = 'input1.txt'

input_int = Ld.tran_input_float(file_name)

X0 = input_int[0]
V0 = input_int[1]
T = input_int[2]
damp = input_int[3]
delta_t = input_int[4]
Time = input_int[5]
m = input_int[6]
Tg = int(Time / delta_t + 1)  # the number of time steps


###### using the potential energy generator to create the potential energy file
#L: the range of movement of the particle
#N: the number of grid, it should be odd number
###### calculate the potential force and input them
# the potential energy surface with function (a-b*x^2)^2
a1 = 5
b1 = 1
L = 8
delta_x = 0.001
pot = PotEneGenSqu.Pot_Energy_Gen(delta_x, L, a1, b1)
pot.output()
inputdata = np.genfromtxt('potential_energy_squarex.txt')
N = np.size(inputdata, 0)
Fp = np.zeros(N)
X_pot = np.zeros(N)
for line in range(N):
    X_pot[line] = round (inputdata[line][1], 3)
    Fp[line] = inputdata[line][3]

data_get = Ld.dynamics(X0, V0, T, damp, delta_t, Time, m, L, X_pot, Fp, Tg)

t_arr,X,V = data_get


out_file = 'output1.txt'
Ld.output_f_v(out_file, Tg, t_arr, X, V)

