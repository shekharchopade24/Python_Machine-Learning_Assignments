########################################################################
# Assignment No 40 - Question 2
# Remove the column SleepHours from the dataset, train the module again
# and compare new accuracy with previous accuracy
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
# Step 2 : Train The Module Using All Feturers
#########################################################

print(Border)
print("Step 2 : Train The Module Using All Feturers")
print(Border)

feture_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feture_cols]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

accuracy_full = accuracy_score(Y_test,Y_pred)

print("Accuracy With All Feturers (Including SleepHours) :",accuracy_full*100)

#########################################################
# Step 3 : Remove SleepHours Colum And Train Again
#########################################################

print(Border)
print("Step 3 : Remove SleepHours Colum And Train Again")
print(Border)

df_new = df.drop("SleepHours",axis=1)

print("SleepHours Colum Removed From Dataset")
print(df_new.head())

feture_cols_new = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted"]

X_new = df_new[feture_cols_new]
Y_new = df_new["FinalResult"]

X_train2,X_test2,Y_train2,Y_test2 = train_test_split(X_new,Y_new,test_size=0.3,random_state=42)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train2,Y_train2)

Y_pred2 = model2.predict(X_test2)

accuracy_new = accuracy_score(Y_test2,Y_pred2)

print("Accuracy Without SleepHours Colum :",accuracy_new*100)

#########################################################
# Step 4 : Compare Both Accuracy
#########################################################

print(Border)
print("Step 4 : Compare Both Accuracy")
print(Border)

print("Accuracy With SleepHours    :",accuracy_full*100)
print("Accuracy Without SleepHours :",accuracy_new*100)

if accuracy_new == accuracy_full:
    print("Removing SleepHours Colum Dose Not Affect The Performence Of Module")
elif accuracy_new > accuracy_full:
    print("Removing SleepHours Colum Improves The Performence Of Module")
else:
    print("Removing SleepHours Colum Decreses The Performence Of Module")
