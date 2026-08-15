import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*50

##################################################
#
#  Step 1 : Load the dataset
#
##################################################

print(Border)
print("Step 1 : Load The Dataset")
print(Border)

DataPath = "student_performance_ml.csv"

# Data Frame
df = pd.read_csv(DataPath)

print("Dataset Loaded Successsfully")

print("First 5 Records From Dataset Are :")
print(df.head())

print("Last 5 Records From Dataset Are :")
print(df.tail())

print("Total Number of Rows and Columns :",df.shape)

print("List of Column names :",list(df.columns))

print("Data types of each column :")
print(df.dtypes)
