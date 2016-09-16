#Colormap_Test.py
 
import colormaps
from colormaps import grab

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import colors as mc

colormap = "3gauss.rgb"
colors, num_colors = grab.main(colormap)
levels = [0, .2, .4, .6, .8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]
cmap = mpl.colors.ListedColormap(colors)
norm = mc.BoundaryNorm(levels, num_colors)
plt.contourf([[0, 3], [0, 3]], levels= levels, cmap=cmap, vmin=0, vmax=3, norm = norm)
plt.show()


