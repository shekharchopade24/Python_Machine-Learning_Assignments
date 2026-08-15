########################################################################
# Assignment No 40 - Question 6
# Identify students where y_test != y_pred, display those rows, count
# how many students were misclassified and observe common pattern
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
# Step 3 : Split, Build And Train The Module
#########################################################

print(Border)
print("Step 3 : Split, Build And Train The Module")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print("Module Trainned And Testing Done")

#########################################################
# Step 4 : Find Misclassified Students
#########################################################

print(Border)
print("Step 4 : Find Misclassified Students")
print(Border)

# Building a result dataframe using the testing feturers so that we can
# see actual values of each student along with expected and predicted result

result_df = X_test.copy()
result_df["ActualResult"] = Y_test
result_df["PredictedResult"] = Y_pred

mismatch_df = result_df[result_df["ActualResult"] != result_df["PredictedResult"]]

print("Misclassified Students Are :")
print(mismatch_df)

print()
print("Total Students In Testing Set :",len(result_df))
print("Total Misclassified Students  :",len(mismatch_df))

#########################################################
# Step 5 : Observe Common Pattern
#########################################################

print(Border)
print("Step 5 : Observe Common Pattern")
print(Border)

if len(mismatch_df) > 0:
    print("Average Feture Values Of Misclassified Students :")
    print(mismatch_df[feture_cols].mean())
    print()
    print("Mostly Misclassified Students Have Boundery Line Values,")
    print("Ex, StudyHours And Attendance Very Close To The Pass/Fail Cutoff")
else:
    print("No Misclassified Students Found, Module Predicted All Correctly")
