########################################################################
# Assignment No 40 - Question 10
# Train module with max_depth = None, calculate training accuracy and
# testing accuracy, explain why training accuracy is 100% but testing
# accuracy is lower
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
# Step 3 : Split The Dataset For Training And Testing
#########################################################

print(Border)
print("Step 3 : Split The Dataset For Training And Testing")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

print("X_train :",X_train.shape)
print("X_test  :",X_test.shape)

#########################################################
# Step 4 : Train Module With max_depth = None
#########################################################

print(Border)
print("Step 4 : Train Module With max_depth = None")
print(Border)

model = DecisionTreeClassifier(max_depth=None,random_state=42)
model.fit(X_train,Y_train)

print("Module Trainned Succesfully With max_depth = None")

#########################################################
# Step 5 : Calculate Training And Testing Accuracy
#########################################################

print(Border)
print("Step 5 : Calculate Training And Testing Accuracy")
print(Border)

Y_train_pred = model.predict(X_train)
Y_test_pred = model.predict(X_test)

training_accuracy = accuracy_score(Y_train,Y_train_pred)
testing_accuracy = accuracy_score(Y_test,Y_test_pred)

print("Training Accuracy :",training_accuracy*100)
print("Testing Accuracy  :",testing_accuracy*100)

#########################################################
# Step 6 : Explaination
#########################################################

print(Border)
print("Step 6 : Explaination")
print(Border)

if training_accuracy == 1.0 and testing_accuracy < training_accuracy:
    print("Training Accuracy Is 100% But Testing Accuracy Is Lower Becouse")
    print("The Tree Is Allowed To Grow Without Any Depth Limit (max_depth=None)")
    print("So It Keeps Spliting The Data Untill Every Single Training Record")
    print("Is Classified Correctly, Even The Noise And Random Variations In")
    print("The Training Data Get Memorised By The Tree")
    print()
    print("This Situation Is Called Overfitting, The Module Learns The")
    print("Training Data By Heart Instead Of Learning The General Pattern,")
    print("So It Performs Very Well On Training Data But Fails To Generalize")
    print("On New Unseen Testing Data, Hence Testing Accuracy Drops Down")
else:
    print("Training Accuracy :",training_accuracy*100)
    print("Testing Accuracy  :",testing_accuracy*100)
    print("In This Run Both Accuracy Are Close To Each Other")
