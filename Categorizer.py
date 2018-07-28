#! /bin/python3

import os
from sys import argv
from config import catig 


try:
	path = argv[1]
except IndexError:
	print("Error: Path to directory is required!")
	exit()

for file in os.listdir(path):
	print("processing:", file)
	ext = file.split(".")[-1]
	if ext in catig.keys():
		print("transferring {} from {} to {} ".format(file, argv[1].split("/")[-1], catig.split("/")[-2]))
		os.rename(os.path.join(path, file), os.path.join(catig[ext], file))
