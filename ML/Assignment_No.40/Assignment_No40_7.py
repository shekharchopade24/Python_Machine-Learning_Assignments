########################################################################
# Assignment No 40 - Question 7
# Train module using random_state = 0, 10, 42 and compare testing
# accuracy, does the result change ?
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
# Step 3 : Train Module With Diffrent random_state Values
#########################################################

print(Border)
print("Step 3 : Train Module With Diffrent random_state Values")
print(Border)

random_states = [0, 10, 42]
accuracy_result = {}

for state in random_states:
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=state)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    accuracy_result[state] = accuracy

    print("random_state =",state," -> Testing Accuracy :",accuracy*100)

#########################################################
# Step 4 : Compare Testing Accuracy
#########################################################

print(Border)
print("Step 4 : Compare Testing Accuracy")
print(Border)

for state,accuracy in accuracy_result.items():
    print("random_state",state,":",accuracy*100)

unique_values = set(accuracy_result.values())

if len(unique_values) == 1:
    print()
    print("Result Dose Not Change, Accuracy Is Same For All random_state Values")
else:
    print()
    print("Result Changes With Diffrent random_state Values")
    print("This Happens Because random_state Controls How The Dataset Gets Split")
    print("Into Training And Testing Part, Diffrent Split Means Diffrent Data")
    print("Is Used For Training And Testing Which Can Change The Accuracy")
