import numpy as np
import PotEneGenSqu as peg

a1 = 5
b1 = 1
L = 10
delta_x = 0.001

c = peg.Pot_Energy_Gen(delta_x, L, a1, b1)

c.output()
