import numpy as np

def spins(L):
    return np.random.choice([-1, 1], size=(L, L))

def dE(spin, i, j):
    L = spin.shape[0]
    delta_E = 2 * spin[i, j] * (
        spin[(i + 1) % L, j] + 
        spin[i, (j + 1) % L] + 
        spin[(i - 1) % L, j] + 
        spin[i, (j - 1) % L]
    )
    return delta_E

def flip_spin(delta_E, T):
    if delta_E < 0 or delta_E >= 0 and np.exp(-delta_E / T) > np.random.rand():
        return True
    
def update_lattice(spin, T):
    N = spin.shape[0]
    for i in range(N):
        for j in range(N):
            delta_E = dE(spin, i, j)
            if flip_spin(delta_E, T):
                spin[i, j] *= -1
    return spin

