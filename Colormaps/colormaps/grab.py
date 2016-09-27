#Grab and return the specified color map

from __future__ import division
import numpy as np
import os
import sys

def get_files():
	prefix = os.getcwd()
	path = prefix + "/colormaps/NCL_color_maps"
	files = os.listdir(path)
	return files

def return_colors(filename):
	#Open file
	prefix = os.getcwd()
	path = prefix + "/colormaps/NCL_color_maps/" + filename
	file = open(path, "r")
	file_contents = []
	for line in file:
		file_contents.append(line)

	#Extract total number of colors
	delim = file_contents[0].index("=") + 1
	num_colors = file_contents[0][delim:]
	num_colors = int(num_colors)

	file_contents = file_contents[2:]
	rgb_list = []

	#Extract RGB values
	for line in file_contents:
		line_contents = line.split(" ")
		while "" in line_contents:
			line_contents.remove("")

		r = line_contents[0]
		g = line_contents[1]
		b = line_contents[2]

		if "." not in r:
			r = float(r) / 255
			g = float(g) / 255
			b = float(b) / 255
		else:
			r = float(r)
			g = float(g)
			b = float(b)

		rgb_list.append([r, g, b])

	rgb_array = np.array(rgb_list, dtype = float)
	return rgb_array, num_colors

def main(argv):
	colormap_files = get_files()
	arg = argv[:-4] + ".rgb"
	if arg in colormap_files:
		rgb_array = return_colors(arg)
		return rgb_array
	#else:
		

if __name__ == "__main__":
	main(sys.argv)