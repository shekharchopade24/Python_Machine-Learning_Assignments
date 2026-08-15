########################################################################
# Assignment No 40 - Question 3
# Train the module using only StudyHours and Attendance and compare
# the accuracy with the full feture module
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
# Step 2 : Train The Module Using All Feturers (Full Module)
#########################################################

print(Border)
print("Step 2 : Train The Module Using All Feturers")
print(Border)

feture_cols_full = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X_full = df[feture_cols_full]
Y_full = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X_full,Y_full,test_size=0.3,random_state=42)

model_full = DecisionTreeClassifier(random_state=42)
model_full.fit(X_train,Y_train)

Y_pred = model_full.predict(X_test)

accuracy_full = accuracy_score(Y_test,Y_pred)

print("Accuracy Of Full Feture Module :",accuracy_full*100)

#########################################################
# Step 3 : Train The Module Using Only StudyHours And Attendance
#########################################################

print(Border)
print("Step 3 : Train Using Only StudyHours And Attendance")
print(Border)

feture_cols_small = ["StudyHours","Attendance"]

X_small = df[feture_cols_small]
Y_small = df["FinalResult"]

X_train2,X_test2,Y_train2,Y_test2 = train_test_split(X_small,Y_small,test_size=0.3,random_state=42)

model_small = DecisionTreeClassifier(random_state=42)
model_small.fit(X_train2,Y_train2)

Y_pred2 = model_small.predict(X_test2)

accuracy_small = accuracy_score(Y_test2,Y_pred2)

print("Accuracy Using Only StudyHours And Attendance :",accuracy_small*100)

#########################################################
# Step 4 : Compare Both Accuracy
#########################################################

print(Border)
print("Step 4 : Compare Both Accuracy")
print(Border)

print("Accuracy Of Full Feture Module           :",accuracy_full*100)
print("Accuracy Of StudyHours + Attendance Module :",accuracy_small*100)

if accuracy_small >= accuracy_full:
    print("Module Is Still Performing Well Even With Only Two Feturers")
else:
    print("Module Performence Drops When We Use Only Two Feturers")
