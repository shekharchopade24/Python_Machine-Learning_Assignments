import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-"*50

##################################################
#
#  Step 1 : Load Dataset and Build Decision Tree Model
#
##################################################

print(Border)
print("Step 1 : Load Dataset and Build Decision Tree Model")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset Loaded Successfully")
print("Initial Entries From Dataset Are :")
print(df.head())

print("Shape of Dataset :",df.shape)
print("Column names :",list(df.columns))

print("Missing Values Per Column :")
print(df.isnull().sum())

# X --> Independent Variables / Features
# Y --> Dependent Variable / Label

X = df.drop(columns = ["FinalResult"])
Y = df["FinalResult"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size = 0.2,random_state = 42
)

print("Dataset Splitting Activity Done")

print("X_train :",X_train.shape)
print("X_test :",X_test.shape)
print("Y_train :",Y_train.shape)
print("Y_test :",Y_test.shape)

model = DecisionTreeClassifier(random_state = 42)

print("Model gets Created Successfully")

model.fit(X_train,Y_train)

print("Model Trained Successfully")

Y_pred = model.predict(X_test)

print("Model Testing Done")

##################################################
#
#  Step 1 : Feature Importance
#
##################################################

print(Border)
print("Feature Importance")
print(Border)

Importance = pd.DataFrame({
    "Feature" : X.columns,
    "Importance" : model.feature_importances_
})

Importance = Importance.sort_values(
    by = "Importance",
    ascending = False
)

print(Importance)

print("Most Important Feature :",
      Importance.iloc[0]["Feature"])

print("Least Important Feature :",
      Importance.iloc[-1]["Feature"])

##################################################
#
#  Step 2 : Remove SleepHours From Dataset
#
##################################################

print(Border)
print("Step 2 : Remove SleepHours From Dataset")
print(Border)

X_New = df.drop(columns = ["SleepHours","FinalResult"])
Y_New = df["FinalResult"]

X_train_New,X_test_New,Y_train_New,Y_test_New = train_test_split(
    X_New,Y_New,test_size = 0.2,random_state = 42
)

model_New = DecisionTreeClassifier(random_state = 42)

model_New.fit(X_train_New,Y_train_New)

Y_pred_New = model_New.predict(X_test_New)

from sklearn.metrics import accuracy_score

OriginalAccuracy = accuracy_score(Y_test,Y_pred)
NewAccuracy = accuracy_score(Y_test_New,Y_pred_New)

print("Original Model Accuracy :",OriginalAccuracy*100)
print("Accuracy After Removing SleepHours :",NewAccuracy*100)

if NewAccuracy > OriginalAccuracy:
    print("Accuracy is improved after removing SleepHours.")

elif NewAccuracy < OriginalAccuracy:
    print("Accuracy is reduced after removing SleepHours.")

else:
    print("Accuracy remains same after removing SleepHours.")

##################################################
#
#  Step 3 : Train Model Using StudyHours and Attendance
#
##################################################

print(Border)
print("Step 3 : Train Model Using Only StudyHours and Attendance")
print(Border)

X_New = df[["StudyHours","Attendance"]]
Y_New = df["FinalResult"]

X_train_New,X_test_New,Y_train_New,Y_test_New = train_test_split(
    X_New,Y_New,test_size = 0.2,random_state = 42
)

model_New = DecisionTreeClassifier(random_state = 42)

model_New.fit(X_train_New,Y_train_New)

Y_pred_New = model_New.predict(X_test_New)

Accuracy_New = accuracy_score(Y_test_New,Y_pred_New)

print("Accuracy Using StudyHours and Attendance :",Accuracy_New*100)

if Accuracy_New >= OriginalAccuracy:
    print("The model is still performing well.")

else:
    print("The model accuracy is reduced when only two features are used.")

##################################################
#
#  Step 4 : Predict Results For 5 New Students
#
##################################################

print(Border)
print("Step 4 : Predict Results For 5 New Students")
print(Border)

NewStudents = pd.DataFrame(
[
    [2,65,45,3,5],
    [5,82,62,6,7],
    [7,90,75,8,8],
    [3,72,52,4,6],
    [8,95,85,9,8]
],
columns = X.columns
)

print("Details of New Students :")
print(NewStudents)

NewPrediction = model.predict(NewStudents)

NewStudents["PredictedResult"] = NewPrediction

print("Predicted Results :")
print(NewStudents)
