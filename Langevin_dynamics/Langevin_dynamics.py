# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import math as mt


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

####### the parameter input 
with open('input.txt', 'r') as intxt:
    for line in intxt: 
        input_stri = line.split()

input_int = map(float, input_stri)

X0 = input_int[0]
V0 = input_int[1]
T = input_int[2]
damp = input_int[3]
delta_t = input_int[4]
Time = input_int[5]
m = input_int[6]


Tg = int( Time/delta_t + 1 )
###### using the potential energy generator to create the potential energy file
###### input parameters are 
#L: the range of movement of the particle
#N: the number of grid, it should be odd number
#U_peak: the highest potnetial energy
#std: the standard variance of the gaussian function

 
###### extracgt the potential force and correspoding position input


inputdata = np.genfromtxt('potential_energy_squarex.txt')

N = np.size(inputdata, 0)

Fp = np.zeros(N)
X_pot = np.zeros(N)

for line in range(N):
    X_pot[line] = round (inputdata[line][1], 3)
    Fp[line] = inputdata[line][3]
     	
###### the solvent force generator(using gaussian distribution)
mean = 0
std = mt.sqrt(2 * mt.sqrt(damp) * T )


x = X0
v = V0

######the evolution

fp =  Fp[0]
V = np.zeros(Tg)
X = np.zeros(Tg)
t_arr = np.linspace(0, Time, Tg)


for t in range(Tg):
 
    Fs = rd.gauss(mean, std)
    a = ( -damp * v  + Fs - fp ) / m
    V[t] = v + delta_t * a   
    X[t] = x + delta_t * V[t]
#the precition is the first three digits after the decimal to pick the corresponding potential force   
# reset the value of x Fs, and fp for the next round
    x = round(X[t], 3)
    v = V[t]
    itemindex = np.where(X_pot == x)[0][0]
    fp = Fp[itemindex] 

##### output the file

with open('output.txt', 'w') as f:
    f.write('#this format is:\n')
    f.write('#index t X V\n')
    for index in range(Tg):
        f.write('{} {} {} {}\n'.format(index + 1, t_arr[index], X[index], V[index]))

