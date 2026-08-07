import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

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
print("Initial Entries From Dataset Are :")
print(df.head())

##################################################
#
#  Step 2 : Decide Independent and Dependent variables
#
##################################################

print(Border)
print("Step 2 : Decide Independent and Dependent variables")
print(Border)

# X --> Independent Variable /Featurs
# Y --> Dependent Variable /Labels

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
    ]

X = df[feature_cols]
Y = df["FinalResult"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

##################################################
#
#  Step 3 : Split the dataset for Trainning and Testing
#
##################################################

print(Border)
print("Step 3 : Split the dataset for Trainning and Testing")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 42)

print("Dataset Spliting activity done")

print("X_train :",X_train.shape)
print("X_test :",X_test.shape)

print("Y_train :",Y_train.shape)
print("Y_test :",Y_test.shape)

##################################################
#
#  Step 4 : Build and Train the Model (Q1)
#
##################################################

print(Border)
print("Step 4 : Build and Train the Model")
print(Border)

model = DecisionTreeClassifier(random_state = 42)

model.fit(X_train,Y_train)

print("Model Created and Trainned Successfuly")

##################################################
#
#  Step 5 : Predict results for X_test (Q2)
#
##################################################

print(Border)
print("Step 5 : Predict results for X_test")
print(Border)

Y_pred = model.predict(X_test)

print("Model Testing Done")

print("Expected Answers :")
print(Y_test.values)

print("Predicted Answerrs :")
print(Y_pred)

##################################################
#
#  Step 6 : Calculate Accuracy using accuracy_score (Q3)
#
##################################################

print(Border)
print("Step 6 : Calculate Accuracy using accuracy_score")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of model is :",accuracy*100,"%")

##################################################
#
#  Step 7 : Generate Confusion Matrix (Q4)
#
##################################################

print(Border)
print("Step 7 : Generate Confusion Matrix")
print(Border)

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix :")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = ["Fail","Pass"])
disp.plot(cmap = "Blues")
plt.title("Marvellous Student Performance Case Study - Confusion Matrix")
plt.show()

# Explanation of Confusion Matrix terms :
# True Positive (TP)  -> Actual Pass, Predicted Pass
# True Negative (TN)  -> Actual Fail, Predicted Fail
# False Positive (FP) -> Actual Fail, Predicted Pass (Model wrongly says Pass)
# False Negative (FN) -> Actual Pass, Predicted Fail (Model wrongly says Fail)

TN,FP,FN,TP = cm.ravel()

print("True Positive :",TP)
print("True Negative :",TN)
print("False Positive :",FP)
print("False Negative :",FN)
