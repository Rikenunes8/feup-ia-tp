import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# ---------
# LOAD DATA
# ---------

droupout_data = pd.read_csv('data/data.csv', na_values=['NA'])
print(droupout_data.describe())

# Check possible classification entries
print(droupout_data['class'].unique())

sb.pairplot(droupout_data.dropna(), hue='class')

# FIRST DATA ANALYSIS
# plt.figure(figsize=(10, 10))

# for column_index, column in enumerate(droupout_data.columns):
#     if column == 'class':
#         continue
#     plt.subplot(2, 2, column_index + 1)
#     sb.violinplot(x='class', y=column, data=droupout_data)

# -------------
# DATA CLEANING
# -------------

# remove redundant/irrelevant attributes
# remove outliers
# correct measures / adjust scale
# deal with missing values
# ... etc ...

# -------------
# SAVE NEW DATA
# -------------

# droupout_data.to_csv('data/data-clean.csv', index=False)
# droupout_data_clean = pd.read_csv('data/data-clean.csv')
# sb.pairplot(droupout_data_clean, hue='class')
