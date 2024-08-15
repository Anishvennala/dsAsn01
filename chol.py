# DS1000 Asn01 question 8
import numpy
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import percentile

chol = pd.read_csv("chol.csv")

sns.boxplot(data=chol, orient="h")
plt.title("Distribution of Risk")
plt.xlabel("Type of People")
plt.ylabel("Cholesterol Levels")

plt.tight_layout()
plt.show()

minimum = np.min(chol.Smokers)
q1 = np.percentile(chol.Smokers, 25)
median = np.median(chol.Smokers)
q3 = np.percentile(chol.Smokers, 75)
maximum = np.max(chol.Smokers)

print("--SMOKERS--")
print("Minimum:", minimum)
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Maximum:", maximum)

print("Mean:" + str(numpy.mean(chol.Smokers)))
print("Standard Deviation:", np.std(chol.Smokers))
print("Count", len(chol.Smokers))

# Calculating quartiles
Q1 = chol.Smokers.quantile(0.25)
Q3 = chol.Smokers.quantile(0.75)

# Calculating IQR
IQR = Q3 - Q1

# Defining the threshold for outliers
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Identifying outliers
outliers = []
for i in range(len(chol.Smokers)):
    if chol.Smokers[i] < lower or chol.Smokers[i] > upper:
        outliers.append(chol.Smokers[i])
        print("Outlier:", chol.Smokers[i], "row:", i)
if outliers == []:
    print("no outlier")


print()

minimum = np.min(chol.Exsmokers)
q1 = np.percentile(chol.Exsmokers, 25)
median = np.median(chol.Exsmokers)
q3 = np.percentile(chol.Exsmokers, 75)
maximum = np.max(chol.Exsmokers)

print("--Ex-SMOKERS--")
print("Minimum:", minimum)
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Maximum:", maximum)

print("Mean:" + str(numpy.mean(chol.Exsmokers)))
print("Standard Deviation:", np.std(chol.Exsmokers))
print("Count", len(chol.Exsmokers))

# Calculating quartiles
Q1 = chol.Exsmokers.quantile(0.25)
Q3 = chol.Exsmokers.quantile(0.75)

# Calculating IQR
IQR = Q3 - Q1

# Defining the threshold for outliers
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Identifying outliers
outliers = []
for i in range(len(chol.Exsmokers)):
    if chol.Exsmokers[i] < lower or chol.Exsmokers[i] > upper:
        outliers.append(chol.Exsmokers[i])
        print("Outlier:", chol.Exsmokers[i], "row:", i)

if outliers == []:
    print("no outlier")

print()