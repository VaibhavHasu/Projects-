# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:06:15 2024

@author: vhasu
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
dataframe = 'C:/vhasu final project/Cleaned_Mental_Health_Data.csv'
df = pd.read_csv(dataframe)
print(df.head())


# Group by 'Indicator' and 'Subgroup' to find average mental health outcomes
grouped_data = df.groupby(['Indicator', 'Subgroup'])['Value'].mean().reset_index()

# Visualization of mental health outcomes by care type and subgroup
sns.barplot(
    x='Indicator', 
    y='Value', 
    hue='Subgroup', 
    data=grouped_data
)
plt.title("Mental Health Outcomes by Indicator and Subgroup")
plt.xticks(rotation=45)
plt.ylabel("Average Outcome")
plt.show()

