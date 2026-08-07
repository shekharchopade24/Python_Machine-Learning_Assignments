########################################################################
# Assignment No 40 - Question 9
# Create a new column PerformanceIndex = (StudyHours * 2) + Attendance
# Train the module including this new feture, does accuracy improve ?
########################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-"*30

#########################################################
# Step 1 : Load The Dataset
#########################################################

print(Border)
print("Step 1 : Load The Dataset")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset Loded Succsesfully")
print(df.head())

#########################################################
# Step 2 : Train The Module Without PerformanceIndex
#########################################################

print(Border)
print("Step 2 : Train The Module Without PerformanceIndex")
print(Border)

feture_cols_old = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X_old = df[feture_cols_old]
Y_old = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X_old,Y_old,test_size=0.3,random_state=42)

model_old = DecisionTreeClassifier(random_state=42)
model_old.fit(X_train,Y_train)

Y_pred_old = model_old.predict(X_test)

accuracy_old = accuracy_score(Y_test,Y_pred_old)

print("Accuracy Without PerformanceIndex :",accuracy_old*100)

#########################################################
# Step 3 : Create New Colum PerformanceIndex
#########################################################

print(Border)
print("Step 3 : Create New Colum PerformanceIndex")
print(Border)

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

print("PerformanceIndex Colum Added Succesfully")
print(df.head())

#########################################################
# Step 4 : Train The Module Including PerformanceIndex
#########################################################

print(Border)
print("Step 4 : Train The Module Including PerformanceIndex")
print(Border)

feture_cols_new = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours","PerformanceIndex"]

X_new = df[feture_cols_new]
Y_new = df["FinalResult"]

X_train2,X_test2,Y_train2,Y_test2 = train_test_split(X_new,Y_new,test_size=0.3,random_state=42)

model_new = DecisionTreeClassifier(random_state=42)
model_new.fit(X_train2,Y_train2)

Y_pred_new = model_new.predict(X_test2)

accuracy_new = accuracy_score(Y_test2,Y_pred_new)

print("Accuracy With PerformanceIndex :",accuracy_new*100)

#########################################################
# Step 5 : Compare Both Accuracy
#########################################################

print(Border)
print("Step 5 : Compare Both Accuracy")
print(Border)

print("Accuracy Without PerformanceIndex :",accuracy_old*100)
print("Accuracy With PerformanceIndex    :",accuracy_new*100)

if accuracy_new > accuracy_old:
    print("Adding PerformanceIndex Improves The Accuracy Of Module")
elif accuracy_new == accuracy_old:
    print("Adding PerformanceIndex Dose Not Change The Accuracy Of Module")
    print("Becouse PerformanceIndex Is Just A Combination Of StudyHours And")
    print("Attendance Which Are Already Present In The Dataset, So It Dose")
    print("Not Add Any New Information To The Decision Tree")
else:
    print("Adding PerformanceIndex Decreses The Accuracy Of Module")
