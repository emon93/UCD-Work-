# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# Array practice
x = [4 , 9 , 6, 3, 1]
print(x [1])

y = np.array(x)
print(y[1])

z = np.array(y < 4)
print(z)

# Subsetting array - include first four elements and 4th element
print(y[0:4])
print(y[3])

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Print out the entire 2nd row of np_baseball
print(np_baseball[1,:])

# Select the entire second column of np_baseball
Second_column = np_baseball[:,1]

# Print 2nd row, 1st column element
print(np_baseball[1,0])

# Arithmetic in 2d array - mulitply by 2 in 2d array np_baseball
conversion_by_two = np.array([2,2])
print(np_baseball*conversion_by_two)

# Average vs Median
import numpy as np
a = [1, 4, 8, 10, 12]
print(np.mean(a))
print(np.median(a))

# Example of array filtering

# Lists received
positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights - (select heights for all np_positions which are 'GK')
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights - (note != can mean does not equal)
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers.
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players.
print("Median height of other players: " + str(np.median(other_heights)))
