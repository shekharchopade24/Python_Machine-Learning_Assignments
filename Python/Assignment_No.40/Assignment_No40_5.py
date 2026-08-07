########################################################################
# Assignment No 40 - Question 5
# Without using accuracy_score, manually calculate accuracy and verify
# whether it matches sklearn accuracy
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
# Step 4 : Manually Calculate Accuracy
#########################################################

print(Border)
print("Step 4 : Manually Calculate Accuracy")
print(Border)

# Reset index so that we can compare values position wise
Y_test_reset = Y_test.reset_index(drop=True)

correct_count = 0
total_count = len(Y_test_reset)

for i in range(total_count):
    if Y_test_reset[i] == Y_pred[i]:
        correct_count = correct_count + 1

manual_accuracy = correct_count / total_count

print("Total Testing Records :",total_count)
print("Correctly Predicted Records :",correct_count)
print("Manually Calculated Accuracy :",manual_accuracy*100)

#########################################################
# Step 5 : Verify With Sklearn Accuracy
#########################################################

print(Border)
print("Step 5 : Verify With Sklearn Accuracy")
print(Border)

sklearn_accuracy = accuracy_score(Y_test,Y_pred)

print("Sklearn Accuracy Score :",sklearn_accuracy*100)
print("Manual Accuracy Score  :",manual_accuracy*100)

if round(manual_accuracy,4) == round(sklearn_accuracy,4):
    print("Both Accuracy Values Are Matching")
else:
    print("Both Accuracy Values Are Not Matching, Please Check Calculation")
