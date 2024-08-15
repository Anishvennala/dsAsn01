#DS1000 Asn01 question 6, a.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import percentile
age = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
smartPhonePercent = [47, 56, 42, 26, 20, 9]
otherPhonePercent = [47, 36, 46, 59, 60, 46]
noPhonePercent = [6, 8, 12, 15, 20, 45]
phoneDic = {'age':age, 'smartPhone': smartPhonePercent, 'otherPhone': otherPhonePercent, 'noPhone': noPhonePercent}
dfPhone = pd.DataFrame(data = phoneDic)
print(dfPhone)
print()
print(dfPhone.columns[1:])
print(dfPhone[['smartPhone', 'otherPhone', 'noPhone']].values)
plt.bar(dfPhone.columns[1:], dfPhone.values[1][1:], color=['blue', 'orange', 'green'])
plt.title(f'Cellphone Ownership Distribution for Age Group 25-34')
plt.xlabel('Cellphone Ownership')
plt.ylabel('Percentage')
plt.show()

