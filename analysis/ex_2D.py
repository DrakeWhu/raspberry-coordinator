import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

# Ask the user for the directory where the dumps are stored
directory = input("Enter the directory where the dumps are stored: ")

if directory.endswith('/'):
    directory = directory[:-1]

ex_data = np.load(f'{directory}/electric_field_ex.npy')

fig, ax = plt.subplots()

ims = []
for i in range(len(ex_data)):
    im = ax.imshow(ex_data[i].T, animated=True)
    if i == 0:
        ax.imshow(ex_data[i].T)
    ims.append([im])

animation = ani.ArtistAnimation(fig, ims, interval=100, blit=False, repeat_delay=1000)
writer = ani.PillowWriter(fps=10)
animation.save(f'{directory}/ex.gif', writer='pillow')