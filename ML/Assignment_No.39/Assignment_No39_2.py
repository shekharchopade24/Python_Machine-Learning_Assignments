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
