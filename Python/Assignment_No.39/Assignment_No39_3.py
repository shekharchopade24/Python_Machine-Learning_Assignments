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
