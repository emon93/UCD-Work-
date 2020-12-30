
# import numpy and matplotlib packages
import numpy as np
from matplotlib import

# arrange graph co-ordinates and plot graph
x = np.arange(1, 15)
y = 1 * x
plt.title("Arsenal premier league goals per game stats in 2020")
plt.xlabel("Game")
plt.ylabel("Goals per Game")
plt.plot(x, y)
plt.show()


