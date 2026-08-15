########################################################################
# Assignment No 40 - Question 4
# Create a new DataFrame with details of 5 new students, use the
# trained module to predict their results and display predictions
########################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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
# Step 2 : Deside Independant And Dependant Veriables
#########################################################

print(Border)
print("Step 2 : Deside Independant And Dependant Veriables")
print(Border)

feture_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feture_cols]
Y = df["FinalResult"]

#########################################################
# Step 3 : Split The Dataset And Train The Module
#########################################################

print(Border)
print("Step 3 : Split The Dataset And Train The Module")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

print("Module Trainned Succesfully")

#########################################################
# Step 4 : Create DataFrame Of 5 New Students
#########################################################

print(Border)
print("Step 4 : Create DataFrame Of 5 New Students")
print(Border)

new_students = pd.DataFrame({
    "StudyHours"           : [1.5, 3.0, 5.5, 7.0, 2.0],
    "Attendance"            : [55, 68, 82, 95, 60],
    "PreviousScore"         : [40, 52, 65, 88, 45],
    "AssignmentsCompleted"  : [2, 4, 6, 9, 3],
    "SleepHours"            : [5, 6, 7, 8, 4]
})

print("Details Of New Students :")
print(new_students)

#########################################################
# Step 5 : Predict Result Of New Students
#########################################################

print(Border)
print("Step 5 : Predict Result Of New Students")
print(Border)

predictions = model.predict(new_students)

new_students["PredictedResult"] = predictions

# Converting 1/0 into readable lable for better display
new_students["PredictedStatus"] = new_students["PredictedResult"].map({1:"Pass",0:"Fail"})

print("Predictions For New Students Are :")
print(new_students)
