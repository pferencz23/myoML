# Matplotlib + Slider (3D)
# In a Jupyter notebook, run: %matplotlib widget
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D       # noqa: F401 (for 3D projection)
from matplotlib.widgets import Slider

def threed_animation(patient_data):


# Example: all_samples is numpy array with shape (10, 16000, 4)
# all_samples[t][i] -> [x,y,z,c]
# We'll assume `all_samples` already exists in your namespace.

    n_time = patient_data.shape[0]  # should be 10

    # initial time index
    t0 = 0
    x = patient_data[t0][:, 0]
    y = patient_data[t0][:, 1]
    z = patient_data[t0][:, 2]    
    c = patient_data[t0][:, 3]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x, y, z, c=c, cmap='viridis', s=10)  # adjust s for marker size
    cb = fig.colorbar(sc, ax=ax, pad=0.1)
    ax.set_title(f'Time index: {t0}')

    # slider axes: [left, bottom, width, height] in figure coords
    ax_slider = plt.axes([0.20, 0.03, 0.60, 0.04])
    slider = Slider(ax_slider, 'time', 0, n_time - 1, valinit=t0, valstep=1)


    def update(val):
        t = int(slider.val)
        x = patient_data[t][:, 0]
        y = patient_data[t][:, 1]
        z = patient_data[t][:, 2]
        c = patient_data[t][:, 3]

        # update 3D offsets
        sc._offsets3d = (x, y, z)

        # update colors
        sc.set_array(c)              # update color array for the PathCollection
        # If color range changes across times, you might want to reset vmin/vmax:
        # sc.set_clim(vmin=c.min(), vmax=c.max())

        ax.set_title(f'Time index: {t}')
        fig.canvas.draw_idle()

    slider.on_changed(update)

    plt.show()