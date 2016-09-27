#List colormap files

import os
import sys

def get_files():
	prefix = os.getcwd()
	path = prefix + "/colormaps/NCL_color_maps"
	files = os.listdir(path)
	return files

def main():
	files = get_files()
	for file in files:
		print file

if __name__ == "__main__":
	main(sys.argv)