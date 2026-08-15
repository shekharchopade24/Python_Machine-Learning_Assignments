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

##################################################
#
#  Step 5 : Analyze effect of StudyHours and Attendance on FinalResult
#
##################################################

print(Border)
print("Step 5 : Analyze effect of StudyHours and Attendance on FinalResult")
print(Border)

AvgStudyHoursPass = df[df["FinalResult"] == 1]["StudyHours"].mean()
AvgStudyHoursFail = df[df["FinalResult"] == 0]["StudyHours"].mean()

AvgAttendancePass = df[df["FinalResult"] == 1]["Attendance"].mean()
AvgAttendanceFail = df[df["FinalResult"] == 0]["Attendance"].mean()

print("Average StudyHours of Passed Students :",AvgStudyHoursPass)
print("Average StudyHours of Failed Students :",AvgStudyHoursFail)

print("Average Attendance of Passed Students :",AvgAttendancePass)
print("Average Attendance of Failed Students :",AvgAttendanceFail)

# Observations (4-5 lines) :
# 1. Passed students have higher Average StudyHours than Failed students.
# 2. Passed students have higher Average Attendance than Failed students.
# 3. This shows StudyHours and Attendance are directly related to passing.
# 4. Students studying less and attending less classes tend to Fail more.
# 5. So higher StudyHours and Attendance increase the chance of passing.

##################################################
#
#  Step 6 : Histogram of StudyHours
#
##################################################

print(Border)
print("Step 6 : Histogram of StudyHours")
print(Border)

plt.figure(figsize = (7,5))
plt.hist(df["StudyHours"], bins = 10, color = "skyblue", edgecolor = "black")

plt.title("Marvellous Student Performance Case Study - StudyHours Distribution")
plt.xlabel("StudyHours")
plt.ylabel("Number of Students")

plt.grid()
plt.show()

# Explanation :
# The histogram shows how StudyHours are distributed among students.
# Most students study within a common range, and very few students
# study for very low or very high hours. This tells us the general
# study pattern followed by the majority of students.

##################################################
#
#  Step 7 : Scatter plot of StudyHours vs PreviousScore
#
##################################################

print(Border)
print("Step 7 : Scatter plot of StudyHours vs PreviousScore")
print(Border)

plt.figure(figsize = (7,5))

for result in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == result]
    label = "Pass" if result == 1 else "Fail"
    plt.scatter(temp["StudyHours"],temp["PreviousScore"],label = label)

plt.title("Marvellous Student Performance Case Study - StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")

plt.legend()
plt.grid()
plt.show()

##################################################
#
#  Step 8 : Boxplot for Attendance
#
##################################################

print(Border)
print("Step 8 : Boxplot for Attendance")
print(Border)

plt.figure(figsize = (7,5))
sns.boxplot(y = df["Attendance"], color = "orange")

plt.title("Marvellous Student Performance Case Study - Attendance Boxplot")
plt.ylabel("Attendance")

plt.grid()
plt.show()

# Observation :
# The boxplot shows the spread of Attendance values along with the
# median, quartiles and any outliers. Points plotted outside the
# whiskers (upper/lower fence) of the boxplot are the outliers,
# meaning those students have unusually high or low Attendance
# compared to the rest of the class.

##################################################
#
#  Step 9 : Relationship between AssignmentsCompleted and FinalResult
#
##################################################

print(Border)
print("Step 9 : Relationship between AssignmentsCompleted and FinalResult")
print(Border)

plt.figure(figsize = (7,5))
sns.boxplot(x = df["FinalResult"], y = df["AssignmentsCompleted"])

plt.title("Marvellous Student Performance Case Study - AssignmentsCompleted vs FinalResult")
plt.xlabel("FinalResult (0 = Fail, 1 = Pass)")
plt.ylabel("AssignmentsCompleted")

plt.grid()
plt.show()

# Observation :
# Students who completed more assignments are mostly found in the
# Pass category, while students with fewer completed assignments
# are mostly found in the Fail category. This shows that completing
# more assignments improves the chances of passing.

##################################################
#
#  Step 10 : SleepHours vs FinalResult
#
##################################################

print(Border)
print("Step 10 : SleepHours vs FinalResult")
print(Border)

plt.figure(figsize = (7,5))
sns.boxplot(x = df["FinalResult"], y = df["SleepHours"])

plt.title("Marvellous Student Performance Case Study - SleepHours vs FinalResult")
plt.xlabel("FinalResult (0 = Fail, 1 = Pass)")
plt.ylabel("SleepHours")

plt.grid()
plt.show()

# Explanation :
# Sleeping more does not directly guarantee success. Passed students
# generally have moderate and consistent SleepHours along with good
# StudyHours and Attendance. Sleep alone is not the deciding factor,
# it works together with StudyHours, Attendance and Assignments to
# affect the FinalResult.
