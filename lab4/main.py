import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches as mpatches
import matplotlib.transforms as mtransforms

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)
ax = plt.axes(xlim=([0, 4*np.pi]), ylim=([-1.3, 1.3]))

bb = mtransforms.Bbox([[-0.3, -0.1], [0.3, 0.1]])
patch = mpatches.FancyBboxPatch((0, 0), abs(bb.width), abs(bb.height), boxstyle=mpatches.BoxStyle("Round", pad=0.05))


def init():
    ax.add_patch(patch)
    return patch,


X = np.linspace(0, 4*np.pi, 100)
Y = np.sin(X)


def animate(i):
    j = i % 100
    patch.set_x(X[j])
    patch.set_y(Y[j])
    return patch,


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=40, blit=True)

plt.show()
anim.save('myAnimation.gif', writer='imagemagick', fps=30)
