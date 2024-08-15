#DS1000 Asn01 question 7
import numpy
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import percentile

cars = pd.read_csv("cars.csv")

plt.hist(cars.Price, bins = 15)
plt.title("Cars")
plt.xlabel("Cars")
plt.ylabel("Frequency")
plt.show()

print("Min:" + str(min(cars.Price)))
print("Max:" + str(max(cars.Price)))
print("Mean:" + str(numpy.mean(cars.Price)))
print("Median:" + str(numpy.median(cars.Price)))

