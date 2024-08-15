#DS1000 Asn01 question 5

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import percentile


sodaList = ['Coca-Cola', 'Diet Coke', 'Dr. Pepper', 'Pepsi', 'Sprite']
percentageList = [35, 15, 20, 22, 8]

sodaDic = {'Soda': sodaList, 'Percentage': percentageList}
df = pd.DataFrame(data = sodaDic)

# Plotting the pie chart
plt.pie(df['Percentage'], labels=df['Soda'], colors = ['brown', 'white', 'red', 'blue', 'green'])
plt.title('Soda Sales Distribution')
plt.show()



