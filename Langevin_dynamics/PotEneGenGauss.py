# generate the potential energy surface and output
#L: the range of movement of the particle
#N:  the number of gird, it should be odd number
#U_peak:  the barrier energy
#std: the standard variance of the gaussian function

from scipy import signal
import numpy as np

class Potential_Energy_Generetor(N, L, U_peak, std):
   
    def space_grid(self, N, L):
    	
        delta_x = L / (N - 1)
	x = np.linspace(0, L, N)
	return x 

    def pot(self, N, U_peak):
	
    	U = U_pe1ak * signal.gaussian(N, self.std)
	return U

    def force(self, L, N):
   	
	U = self.pot(N, std, U_peak)
        F = np.zeros(N)
        #force here using the first order approximation
	for ii in range(N - 1):
            F[ii] = (U[ii+1] - U[ii]) / delta_x
 	    F[N - 1] = 0
        
    def output(self, N )        
        
        x = self.space_grid(N, L)
        U = self.pot(N, std, U_peak)
        F = self.force(self, L, N)
        with open('potential_energy.txt', 'w') as f:
    	    f.write('#this format is:\n')
    	    f.write('#index x U(x) F(x)\n')
            for index in range(N):
        	f.write('{} {} {} {}\n'.format(index + 1, x[index], U[index], F[index]))
 



