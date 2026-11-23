import pandas as pd
import numpy as np 

def load_and_clean_data(df):
"""
Automated Data Cleaning & Transformation Pipeline
Author: Krishna Chand Gupta | Senior Data Analyst & MIS Specialist
""" 

#### 1. Remove duplicate records

initial_rows = len(df)
df = df.drop_duplicates().copy() 

#### 2. Standardize column names

df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns] 

#### 3. Handle missing values (Numerical -> Median, Categorical -> Mode)

for col in df.select_dtypes(include=[np.number]).columns:
df[col] = df[col].fillna(df[col].median()) 

for col in df.select_dtypes(include=['object']).columns:
df[col] = df[col].fillna(df[col].mode()) 

# 4. Cap outliers using IQR method on numeric columns

for col in df.select_dtypes(include=[np.number]).columns:
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df[col] = np.clip(df[col], lower_bound, upper_bound)

print(f"Pipeline Complete: Cleaned {initial_rows - len(df)} duplicate rows. Final shape: {df.shape}")
return df

if **name** == "**main**": 

#### Sample dataset simulation for demonstration

sample_data = pd.DataFrame({
'Customer ID':,
'Monthly Charges': [50.5, np.nan, np.nan, 89.0, 500.0],
'Contract Type': ['Month-to-month', 'One year', 'One year', None, 'Two year']
})
cleaned_df = load_and_clean_data(sample_data)
print(cleaned_df)
