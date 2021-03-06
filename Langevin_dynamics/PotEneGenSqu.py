# generate the potential energy surface with function (a-b*x^2)^2 and output
#L: the range of movement of the particle
#N:  the number of gird

import numpy as np


class Pot_Energy_Gen(object):
    def __init__(self, delta_x, L, a, b):
        self.delta_x = delta_x
        self.L = L
        self.a = a
        self.b = b
        self.N = int(self.L / self.delta_x + 1)
    def space_grid(self):
        x = np.linspace(0, self.L, self.N)
        return x 
    def pot(self):
        x = self.space_grid()
        X = x - self.L / 2
        U = (self.a - self.b * X ** 2) ** 2
        return U
    def force(self):
        x = self.space_grid()
        U = self.pot()
        X = x - self.L / 2
        F = -4 * self.b * (self.a - self.b * X ** 2) * X
        return F
