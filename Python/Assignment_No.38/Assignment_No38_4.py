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

##################################################
#
#  Step 2 : Total students, Pass and Fail count
#
##################################################

print(Border)
print("Step 2 : Total students, Pass and Fail count")
print(Border)

TotalStudents = df.shape[0]
print("Total Number of Students in Dataset :",TotalStudents)

PassCount = df[df["FinalResult"] == 1].shape[0]
FailCount = df[df["FinalResult"] == 0].shape[0]

print("Number of Students Passed :",PassCount)
print("Number of Students Failed :",FailCount)

##################################################
#
#  Step 3 : Statistical Analysis using pandas functions
#
##################################################

print(Border)
print("Step 3 : Statistical Analysis using pandas functions")
print(Border)

AvgStudyHours = df["StudyHours"].mean()
AvgAttendance = df["Attendance"].mean()
MaxPreviousScore = df["PreviousScore"].max()
MinSleepHours = df["SleepHours"].min()

print("Average StudyHours :",AvgStudyHours)
print("Average Attendance :",AvgAttendance)
print("Maximum PreviousScore :",MaxPreviousScore)
print("Minimum SleepHours :",MinSleepHours)

##################################################
#
#  Step 4 : Distribution of FinalResult using value_counts()
#
##################################################

print(Border)
print("Step 4 : Distribution of FinalResult")
print(Border)

print("Value counts of FinalResult :")
print(df["FinalResult"].value_counts())

PassPercentage = (PassCount / TotalStudents) * 100
FailPercentage = (FailCount / TotalStudents) * 100

print("Pass Percentage :",PassPercentage)
print("Fail Percentage :",FailPercentage)

# Observation :
# The dataset is slightly imbalanced / nearly balanced depending on
# actual counts, since Pass and Fail percentages are compared above.
# A dataset is considered balanced when Pass % and Fail % are close
# to 50-50. If the difference is large, the dataset is imbalanced.
