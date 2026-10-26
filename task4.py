"""
This is the template for coding tasks in exercise sheet 1.

Everywhere you see "YOUR CODE", it means a playground for you :P

WARNING: do not rename variables as this will break the tests.
=============================================================================================================================

Through this exercise, you will get to know the basic usage of NumPy and Matplotlib, i.e. frequently used functions/methods.
Because it is the starting point, we thought some referrences to the official documentation will ease the process.

PRECAUTION: you don't need to read through every details in the documentation, that is way too overkill. In most cases, 
grasp a rough idea of how to call a function/method with minimal arguments, and you are good to start writing your own code! 
Many typically offer some examples, which are even more intuitive. As for optional parameters, you can return to them later 
when the minimal use case cannot fulfill your demand.


We are dealing with vectors and matrices in this course, so you will need a NumPy array to store these kind of data.
Beside the classic "np.array()" function, a few functions by specifying a shape can sometimes be very handy:
    <https://numpy.org/doc/stable/reference/routines.array-creation.html#from-shape-or-value>

After you have your arrays, you can apply operators (+, -, *, /, =, ** as exponent) to them at ease. NumPy also provides 
various methods for more advanced operations, for example, the mean value:
    <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html>
Of course, you don't have to use it. There is always more than one solution to a problem.

Quite often, you want to do something with only a part of the array, such as, a single element, a specific row/column, 
a few rows/columns, etc. This is achieved by properly indexing and slicing:
    <https://numpy.org/doc/stable/user/basics.indexing.html#basic-indexing>


After the calculation, it is the exciting moment to show them off in the plots!

The "plt.figure()" function (code already written for this exercise) will create and/or switch to a plot. Then you can call 
various Pyplot functions to draw on the plot.

To draw a line:
    <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html>

To draw a histogram:
    <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html>

Optionally, you can also add title / xlabel / ylabel / legend to make your plot fancier.


Have fun!
"""


import os
import matplotlib.pyplot as plt
import numpy as np


Nmax = 1000 # number of samples
M = 200  # number of experiments

# locate the data file
filepath = os.path.join(os.path.dirname(__file__), "exercise1_dataset.npz")
# load exercise data
data = np.load(filepath)
u = data['u']
i = data['i']


## (a)
# YOUR CODE: calculate the values
# ===============================
# "None" is just to pass the syntax check. Replace them with your code. Don't need to stick to a single line.
# (The same holds for all the following cases)
R_SA_single = np.zeros((Nmax,1))
R_LS_single = np.zeros((Nmax,1))
R_EV_single = np.zeros((Nmax,1))
for k in range(0,Nmax):
    R_SA_single[k,0] = None
    R_LS_single[k,0] = None
    R_EV_single[k,0] = None


plt.figure(1)
# YOUR CODE: draw on the plot 

## (b)
# YOUR CODE: calculate the values
R_SA = np.zeros((Nmax,M))
R_LS = np.zeros((Nmax,M))
R_EV = np.zeros((Nmax,M))

for k in range(Nmax):
    R_SA[k,:] = None
    R_LS[k,:] = None
    R_EV[k,:] = None

plt.figure(2)
# YOUR CODE: draw on the plot 


plt.figure(3)
# YOUR CODE: draw on the plot 


plt.figure(4)
# YOUR CODE: draw on the plot 


## (c)
# YOUR CODE: calculate the values
R_SA_mean = None
R_LS_mean = None
R_EV_mean = None

plt.figure(5)
# YOUR CODE: draw on the plot 


## (d)
# YOUR CODE: calculate the values
R_SA_Nmax = None
R_LS_Nmax = None
R_EV_Nmax = None

plt.figure(6)
# YOUR CODE: draw on the plot 

plt.figure(7)
# YOUR CODE: draw on the plot 

plt.figure(8)
# YOUR CODE: draw on the plot 


# show all plots
# ===============
# If you don't see any plots but also no errors, it is very likely because a non-interactive backend is chosen by default.
# One possible solution you can try is to manually select another backend via "matplotlib.use()" function at the beginning.
# Here gives more details: <https://matplotlib.org/stable/users/explain/backends.html>
plt.show()
