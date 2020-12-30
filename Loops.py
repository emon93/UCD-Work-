# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
       offset = offset - 1
    else :
       offset = offset + 1
    print(offset)

#indexes and values in for loop

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for x, y in enumerate(areas) :
   print("room " + str(x) + ": " + str(y))

#no enumerate function - no indexes included
for a in areas :
    print(a)

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))

#Loop over a list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

for x,y in house :
    print('the ' + str(x) + ' is ' +  str(y) + ' sqm')

# Loop over dictionary

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for x, y in europe.items():
    print("the capital of " + str(x) + " is " + str(y))

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

#Loops over numpy

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Lists received
positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

for x in np_heights :
    print(str(x) + " inches")

# For loop over np_baseball
for y in np.nditer(np_baseball) :
    print(y)

print(np_baseball)

import pandas as pd
products = {'Product': ['Tablet','iPhone','Laptop','Monitor'],
            'Price': [250,800,1200,300]
            }

df_products = pd.DataFrame(products)

for lab,row in df_products.iterrows():
    print(lab,row[0:2])











