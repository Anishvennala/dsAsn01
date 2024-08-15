#DS1000 Asn01 question 6, b.
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
# Extracting data for plotting
age_groups = dfPhone['age']
smartphonePercentages = dfPhone['smartPhone']
otherphonePercentages = dfPhone['otherPhone']
nophonePercentages = dfPhone['noPhone']
# Plotting bars for each phone type
plt.bar(age_groups, smartphonePercentages, label='Smartphone')
plt.bar(age_groups, otherphonePercentages, bottom=smartphonePercentages, label='Other Phone')
plt.bar(age_groups, nophonePercentages, bottom=smartphonePercentages+otherphonePercentages, label='No Phone')
# Adding labels and title
plt.xlabel('Age Group')
plt.ylabel('Percentage')
plt.title('Phone Ownership by Age Group')
# Adding legend
plt.legend(title='Phone Type', bbox_to_anchor=(1.05, 1))
# Show plot
plt.tight_layout()
plt.show()
