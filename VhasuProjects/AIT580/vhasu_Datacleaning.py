# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:55:01 2024

@author: vhasu
"""

import pandas as pd

# Load the Excel file
dataframe = 'C:/vhasu final project/Mental_Health_Care_in_the_Last_4_Weeks.csv'
df = pd.read_csv(dataframe)
print(df.head())



# Cleaning steps:
# 1. Check for missing values
print(df.isnull().sum())

# 2. Drop columns with a high percentage of missing values (if any)
threshold = 0.5  # Adjust as needed
df_cleaned = df.dropna(axis=1, thresh=int(df.shape[0] * threshold))

# 3. Fill or drop rows with missing values
df_cleaned = df_cleaned.dropna()  # Drop rows with missing values
# Alternatively, use data_cleaned.fillna(value) to fill them

# 4. Convert data types if necessary
# Example: data_cleaned['column_name'] = data_cleaned['column_name'].astype(int)

# 5. Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Save the cleaned dataset
df_cleaned.to_csv('C:/vhasu final project/Cleaned_Mental_Health_Data.csv', index=False)

print("Cleaning complete. Cleaned data saved to 'Cleaned_Mental_Health_Data.csv'.")
