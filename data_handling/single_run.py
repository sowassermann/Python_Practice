"""
Script for a single run of the model, with data exported as a dataframe and/or
plotted with matplotlib. A script for multiple runs of the model under the
same conditions can be found in data_batch.py.

Data are collected in the data_collectors.py script and are:
    1. Polarization: a function returning the median absolute deviation of
       agent heading from the mean heading of the group
    2. Nearest neighbour distance: the mean distance of the 5 nearest agents,
       determined using a k-distance tree.
    3. Shoal Area: convex hull
    4. Mean Distance From Centroid

A single run isn't going to be very useful for analysis, but it is useful for
quickly testing the model performance or R code.
"""

from shoal_model import *
import os
import matplotlib.pyplot as plt

# path = "/Users/user/Desktop/Local/Mackerel/Mackerel Data"
path = "/Users/Sophie/Desktop/DO NOT ERASE/1NUIG/Mackerel/Mackerel Data"  # for laptop


# Collect the data from a single run with x number of steps into a dataframe
model = ShoalModel(n_fish=1000,
                   width=1000,
                   height=1000,
                   speed=20,
                   vision=100,
                   separation=10,
                   cohere=0.26,
                   separate=0.26,
                   match=0.59)
for i in range(20):
    model.step()
data = model.datacollector.get_model_vars_dataframe()
data.columns = ["cent", "nnd", "polar", "area"]

# data.to_csv(os.path.join(path, r"single_run.csv"))  # save data to use in R


# DATA COLLECTOR PLOTS --------------------------------------------------------

# plt.style.use("dark_background")
# fig = plt.figure(figsize=(8, 5), dpi=300)
# ax1 = plt.subplot(2, 2, 1)
# plt.xlabel("Distance from Centroid")
#
# ax2 = plt.subplot(2, 2, 2)
# plt.xlabel("Nearest Neighbour Distance")
#
# ax3 = plt.subplot(2, 2, 3)
# plt.xlabel("Polarization")
#
# ax4 = plt.subplot(2, 2, 4)
# plt.xlabel("Shoal Area")
#
# ax1.plot(data["Mean Distance from Centroid"])
# ax2.plot(data["Nearest Neighbour Distance"])
# ax3.plot(data["Polarization"])
# ax4.plot(data["Shoal Area"])
#
# plt.tight_layout()
# plt.show()
