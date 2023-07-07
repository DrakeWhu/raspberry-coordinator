import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

# Ask the user for the directory where the dumps are stored
directory = input("Enter the directory where the dumps are stored: ")

if directory.endswith('/'):
    directory = directory[:-1]

ex_data = np.load(f'{directory}/electric_field_ex.npy')

fig, ax = plt.subplots()
x = np.arange(3072)

def animate(i):
    ax.cla()
    ex_row = ex_data[i][:, 384]
    ax.plot(x, ex_row)
    ax.set_xlabel('ζ = x-ct (μm)')

    # Set the x-axis ticks and labels
    x_ticks = np.linspace(0, 3072, 5)
    x_tick_labels = [f'{tick/100:.2f}' for tick in x_ticks]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_tick_labels)

    ax.set_ylim(-0.1e11, 0.1e11)
    ax.set_ylabel('Ex (V/m)')
    ax.set_title(f'Ex - Row 384 - Dump {i}')

animation = ani.FuncAnimation(fig, animate, frames=len(ex_data), interval=100, repeat_delay=1000)

animation.save(f'{directory}/ex_1D.gif', writer='pillow')