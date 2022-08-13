#!/usr/bin/env python3

#	This code reads a density file in text 
#	mode, and parses the water density

import matplotlib.pyplot as plt 
import numpy as np
import scipy 
import os
from scipy import optimize 


folder = os.path.dirname(__file__)


#	Absolute path to folder in which the files of analysis reside 

densities = os.path.join(folder,"../MassDensities/100")
paths = [ os.path.join(densities,name) for name in os.listdir(densities) ]

data = []


#	Iterate through all files so now allFiles[0] holds the 
#	first file loaded, allFiles[1] holds the second, etc..

for path in paths:
	with open(path,'r') as file: 
		lines = file.readlines()
		data.append(lines)


#	Checking 

print("First File")
print(data[0])
print("Second File")
print(data[1])
print("Third File")
print(data[2])
print("Fourth File")
print(data[3])
print("Fifth File")
print(data[4])
