import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def draw(verts):

    path = Path(verts)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor='orange', lw=3)
    ax.add_patch(patch)
    plt.show()