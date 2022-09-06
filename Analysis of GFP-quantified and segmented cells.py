import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# load raw data file
data = pd.read_csv('ParameterData_Main.txt', sep='\t')

# remove cells out of gate (ROI)
data = data[data['R01'] == 1].reset_index(drop=True)

# rename wells according to wanted comparisons
# s6-8 (1) vs s18-20 (2)
# s10-12 (3) vs s22-24 (4)
# s34-36 (5) vs s58-60 (6)
strains_dict = {6: 1, 7: 1, 8: 1, 18: 2, 19: 2, 20: 2,
                10: 3, 11: 3, 12: 3, 22: 4, 23: 4, 24: 4,
                34: 5, 35: 5, 36: 5, 58: 6, 59: 6, 60: 6}
# remove unwanted wells for the data
data = data[data['Well '].isin(list(strains_dict.keys()))]
data['strain'] = data['Well '].replace(strains_dict)

# sample 500 cells from each wanted well and export data for plotting
sampled_data = pd.DataFrame()
for s in range(1, 7):
    sampled_data = pd.concat([sampled_data, data[data['strain'] == s].sample(n=500)])
# export data for plotting to csv
sampled_data.to_csv('sampled data.csv', index=False)

# plot
# s6-8 (1) vs s18-20 (2)
sns.boxplot(data=sampled_data[np.logical_or(sampled_data['strain'] == 1, sampled_data['strain'] == 2)],
            x='strain', y='Mean Intensity mCherry')
plt.show()
# s10-12 (3) vs s22-24 (4)
sns.boxplot(data=sampled_data[np.logical_or(sampled_data['strain'] == 3, sampled_data['strain'] == 4)],
            x='strain', y='Mean Intensity mCherry')
plt.show()
# s34-36 (5) vs s58-60 (6)
sns.boxplot(data=sampled_data[np.logical_or(sampled_data['strain'] == 5, sampled_data['strain'] == 6)],
            x='strain', y='Mean Intensity mCherry')
plt.show()



# calculate t test and p value
# s6-8 (1) vs s18-20 (2)
s1_s2 = stats.ttest_ind(sampled_data[sampled_data['strain'] == 1]['Mean Intensity mCherry'],
                        sampled_data[sampled_data['strain'] == 2]['Mean Intensity mCherry'])

print('strain 1 (6-8) vs. strain 2 (18-20):')
print('t-statistic: ' + str(s1_s2[0]))
print('p value: ' + str(s1_s2[1]))
# s10-12 (3) vs s22-24 (4)
s3_s4 = stats.ttest_ind(sampled_data[sampled_data['strain'] == 3]['Mean Intensity mCherry'],
                        sampled_data[sampled_data['strain'] == 4]['Mean Intensity mCherry'])

print('strain 3 (10-12) vs. strain 4 (22-24):')
print('t-statistic: ' + str(s3_s4[0]))
print('p value: ' + str(s3_s4[1]))
# s34-36 (5) vs s58-60 (6)
s5_s6 = stats.ttest_ind(sampled_data[sampled_data['strain'] == 5]['Mean Intensity mCherry'],
                        sampled_data[sampled_data['strain'] == 6]['Mean Intensity mCherry'])

print('strain 5 (34-36) vs. strain 6 (58-60):')
print('t-statistic: ' + str(s5_s6[0]))
print('p value: ' + str(s5_s6[1]))