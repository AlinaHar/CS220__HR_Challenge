import os 
from shutil import copy 
from concurrent.futures import ProcessPoolExecutor

all_files = os.listdir('/home/alina/Desktop/python_files/')
executor = ProcessPoolExecutor(15)
for file in all_files:
	ff = os.path.join('/home/alina/Desktop/python_files/', file)
	future = executor.submit(copy, ff, '/home/alina/Desktop/python_copied_files/') 
