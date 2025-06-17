import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from metropolis_hastings import spins, update_lattice

def spin_colors(spin):
    # Red for +1, Blue for -1
    color_map = np.empty(spin.shape, dtype=object)
    color_map[spin == 1] = 'red'
    color_map[spin == -1] = 'blue'
    return color_map.ravel()

def main():
    L = 10
    T = 2.0
    spin = spins(L)

    X, Y = np.meshgrid(np.arange(L), np.arange(L))
    U = np.zeros((L, L))       # No x-component
    V = spin                   # y-component is spin value (up/down)
    C = spin_colors(spin)      # color array based on spins

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    q = ax.quiver(X, Y, U, V, color=C, pivot='middle', scale=20, headwidth=2, headlength=2)
    ax.set_title(f'Temperature: {T:.2f}')
    ax.set_xlim(-1, L)
    ax.set_ylim(-1, L)
    ax.set_aspect('equal')
    ax.axis('off')

    axcolor = 'lightgoldenrodyellow'
    axtemp = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
    stemp = Slider(axtemp, 'Temperature', 0.1, 5.0, valinit=T)

    def update(val):
        nonlocal spin
        T = stemp.val
        spin = update_lattice(spin, T)
        V = spin
        C = spin_colors(spin)
        q.set_UVC(U, V)
        q.set_color(C)
        ax.set_title(f'Temperature: {T:.2f}')
        fig.canvas.draw_idle()

    stemp.on_changed(update)
    plt.show()

if __name__ == "__main__":
    main()
