#!/usr/bin/env python

import csv
import matplotlib.pyplot as plt
import pandas as pd


# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# Bring in the data
data = pd.read_csv('trgn599.clinical.csv', sep=',',header=None, index_col =19) #to see different data from a separate column plotted, change the index col to desired column.

plt.show()
# Plot the histogram
plt.hist(k)

# Save the histogram
plt.savefig('hist.png')

# Display the plot
# plt.show()
