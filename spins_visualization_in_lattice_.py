import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def spins(L):
    """
    Generate a 2D Ising model lattice with random spins.
    
    Parameters:
    L (int): Size of the lattice (LxL).
    
    Returns:
    np.ndarray: A 2D array representing the lattice with random spins.
    """
    return np.random.choice([-1, 1], size=(L, L))

def dE(spin, i, j):
    N = spin.shape[0]
    delta_E = 2 * spin[i, j] * (
        spin[(i + 1) % N, j] + 
        spin[i, (j + 1) % N] + 
        spin[(i - 1) % N, j] + 
        spin[i, (j - 1) % N]
    )
    return delta_E

def flip_spin(delta_E, T):
    if delta_E < 0:
        return True
    else:
        return np.random.rand() < np.exp(-delta_E / T)
    
def update_lattice(spin, T):
    N = spin.shape[0]
    for i in range(N):
        for j in range(N):
            delta_E = dE(spin, i, j)
            if flip_spin(delta_E, T):
                spin[i, j] *= -1
    return spin

def visualize_lattice(spin, T):
    plt.imshow(spin, cmap='gray', vmin=-1, vmax=1)
    plt.title(f'Temperature: {T}')
    plt.axis('off')
    plt.show()

def main():
    L = 20  # Size of the lattice
    T = 2.0  # Temperature
    spin = spins(L)  # Initialize the lattice

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    
    img = ax.imshow(spin, cmap='gray', vmin=-1, vmax=1)
    ax.set_title(f'Temperature: {T}')
    ax.axis('off')

    # Slider for temperature
    axcolor = 'lightgoldenrodyellow'
    axtemp = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
    stemp = Slider(axtemp, 'Temperature', 0.1, 5.0, valinit=T)

    def update(val):
        nonlocal spin
        T = stemp.val
        spin = update_lattice(spin, T)
        img.set_data(spin)
        ax.set_title(f'Temperature: {T}')
        fig.canvas.draw_idle()

    stemp.on_changed(update)

    plt.show()

if __name__ == "__main__":
    main()