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
