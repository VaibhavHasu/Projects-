# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:11:40 2024

@author: vhasu
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the Excel file
dataframe = 'C:/vhasu final project/Cleaned_Mental_Health_Data.csv'
df = pd.read_csv(dataframe)
print(df.head())

# Group by 'Group' (demographic) and 'State' (socio-economic factor), calculating the mean 'Value' (service availability)
availability_by_demographics = df.groupby(['Group', 'State'])['Value'].mean().reset_index()

# Display the result
print(availability_by_demographics)

# Visualize the differences in service availability by Group and State
sns.barplot(x='Group', y='Value', hue='State', data=availability_by_demographics)
plt.title("Mental Health Service Availability by Demographic and Socio-Economic Factors")
plt.xticks(rotation=45)
plt.ylabel("Average Service Availability")
plt.show()

