########################################################################
# Assignment No 40 - Question 1
# After training the Decision Tree model, display feature_importances_
# and find which feture contributes most and which contributes least
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
print("Initial Entries From Dataset Are")
print(df.head())

#########################################################
# Step 2 : Deside Independant And Dependant Veriables
#########################################################

print(Border)
print("Step 2 : Deside Independant And Dependant Veriables")
print(Border)

# X : Independant Veriables / Feturers
# Y : Dependant Veriable / Lable

feture_cols = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]

X = df[feture_cols]
Y = df["FinalResult"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

#########################################################
# Step 3 : Split The Dataset For Training And Testing
#########################################################

print(Border)
print("Step 3 : Split The Dataset For Training And Testing")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

print("X_train :",X_train.shape)
print("X_test :",X_test.shape)
print("Y_train :",Y_train.shape)
print("Y_test :",Y_test.shape)

#########################################################
# Step 4 : Build And Train The Module
#########################################################

print(Border)
print("Step 4 : Build And Train The Module")
print(Border)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

print("Decision Tree Module Trainned Succesfully")

#########################################################
# Step 5 : Display Feature Importance
#########################################################

print(Border)
print("Step 5 : Display Feature Importance")
print(Border)

importances = model.feature_importances_

print("Feture Importance Score Of Each Column :")
for col,score in zip(feture_cols,importances):
    print(col,":",round(score,4))

# Finding the most and least contributing feture
max_pos = importances.argmax()
min_pos = importances.argmin()

print()
print("Feture Which Contributes Most In Predicting FinalResult :",feture_cols[max_pos])
print("Feture Which Contributes Least In Predicting FinalResult :",feture_cols[min_pos])
