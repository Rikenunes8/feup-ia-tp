from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

# ---------
# LOAD DATA
# ---------

data = pd.read_csv('data/data.csv', na_values=['NA'])
pd.set_option('display.max_columns', None)
print(data.describe())

# Check possible classification entries
print(data['class'].unique())

# sb.pairplot(data.dropna(), hue='class')

# FIRST DATA ANALYSIS

plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})

columns = data.columns[:-1]
pairs = [(columns[i], columns[j]) for i in range(len(columns) - 1) for j in range(i+1, len(columns))]
for column1, column2 in pairs:
    x = data[column1]
    y = data[column2]

    plt.scatter(x, y, label= f'y2 Correlation = {np.round(np.corrcoef(x,y)[0,1], 2)}')
    plt.title(column1 + ' vs ' + column2)
    plt.legend()
    plt.show()


# -------------
# DATA CLEANING
# -------------

# remove redundant/irrelevant attributes

# data = data.drop(['Curricular units 1st sem (credited)', 'Curricular units 1st sem (without evaluations)', 
#             'Curricular units 2nd sem (credited)', 'Curricular units 2nd sem (without evaluations)'], axis=1)
# print(data.describe())

# remove outliers
# correct measures / adjust scale
# deal with missing values
# ... etc ...


# -------------
# SAVE NEW DATA
# -------------

# data.to_csv('data/data-clean.csv', index=False)
# data_clean = pd.read_csv('data/data-clean.csv')
# sb.pairplot(data_clean, hue='class')
