 
from shutil import copy 
import os


all_files = os.listdir('/home/alina/Desktop/python_files/')
for file in all_files:
	ff = os.path.join('/home/alina/Desktop/python_files/', file)
	copy(ff, '/home/alina/Desktop/python_copied_files/')
