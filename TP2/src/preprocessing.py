from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

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
# plt.figure(figsize=(10, 10))

# for column_index, column in enumerate(data.columns):
#     if column == 'class':
#         continue
#     plt.subplot(2, 2, column_index + 1)
#     sb.violinplot(x='class', y=column, data=data)

# -------------
# DATA CLEANING
# -------------

# remove redundant/irrelevant attributes

data = data.drop(['Curricular units 1st sem (credited)', 'Curricular units 1st sem (without evaluations)', 
            'Curricular units 2nd sem (credited)', 'Curricular units 2nd sem (without evaluations)'], axis=1)
print(data.describe())

# remove outliers
# correct measures / adjust scale
# deal with missing values
# ... etc ...





# -------------
# SAVE NEW DATA
# -------------

data.to_csv('data/data-clean.csv', index=False)
# data_clean = pd.read_csv('data/data-clean.csv')
# sb.pairplot(data_clean, hue='class')
