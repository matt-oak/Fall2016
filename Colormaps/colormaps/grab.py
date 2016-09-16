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

def return_file(filename):
	prefix = os.getcwd()
	path = prefix + "/colormaps/NCL_color_maps/" + filename
	file = open(path, "r")
	file_contents = []
	for line in file:
		file_contents.append(line)

	num_rows = int(file_contents[0][-4:-1])
	file_contents = file_contents[2:]
	rgb_list = []

	for line in file_contents:
		line_contents = line.split(" ")
		while "" in line_contents:
			line_contents.remove("")
		r = float(line_contents[0])/255
		g = float(line_contents[1])/255
		b = float(line_contents[2][-4:-1])/255
		rgb_list.append([r, g, b])

	rgb_array = np.array(rgb_list, dtype = float)
	return rgb_array, num_rows


def main(argv):
	colormap_files = get_files()
	arg = argv[:-4] + ".rgb"
	if arg in colormap_files:
		rgb_array = return_file(arg)
		return rgb_array
	#else:
		

if __name__ == "__main__":
	main(sys.argv)