import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

##################################################
#
#  Function : CheckAccuracy
#  Splits dataset into Training and Testing data
#  and calculates accuracy by changing value of K
#
##################################################

def CheckAccuracy(X,Y):
    border = "-"*40

    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.5,random_state = 42)

    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)
    print(border)

    k_values = [1,3,5,7]

    for k in k_values:
        model = KNeighborsClassifier(n_neighbors = k)
        model = model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test,Y_pred)

        print("K =",k," Accuracy :",accuracy*100,"%")

    print(border)

##################################################
#
#  Function : MarvellousClassifier
#
##################################################

def MarvellousClassifier(DataPath):
    border = "-"*40

    # Step 1 : Get Data
    print(border)
    print("Step 1 : Get Data")
    print(border)

    df = pd.read_csv(DataPath)

    print("Some Entries from Dataset :")
    print(df.head())
    print("Shape of dataset :",df.shape)
    print(border)

    # Step 2 : Clean, Prepare and Manipulate data
    print(border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(border)

    WetherLE = LabelEncoder()
    TemperatureLE = LabelEncoder()
    PlayLE = LabelEncoder()

    df["Wether"] = WetherLE.fit_transform(df["Wether"])
    df["Temperature"] = TemperatureLE.fit_transform(df["Temperature"])
    df["Play"] = PlayLE.fit_transform(df["Play"])

    print("Dataset After Encoding :")
    print(df.head())
    print(border)

    print("Wether Classes :",list(WetherLE.classes_))
    print("Temperature Classes :",list(TemperatureLE.classes_))
    print("Play Classes :",list(PlayLE.classes_))
    print(border)

    X = df[["Wether","Temperature"]]
    Y = df["Play"]

    # Step 3 : Train Data
    print(border)
    print("Step 3 : Train Data")
    print(border)

    model = KNeighborsClassifier(n_neighbors = 3)
    model = model.fit(X,Y)

    print("Model Trainned Successfuly on Whole Dataset")
    print(border)

    # Step 4 : Test Data
    print(border)
    print("Step 4 : Test Data")
    print(border)

    TestWether = "Sunny"
    TestTemperature = "Cool"

    EncodedWether = WetherLE.transform([TestWether])[0]
    EncodedTemperature = TemperatureLE.transform([TestTemperature])[0]

    TestPoint = pd.DataFrame([[EncodedWether,EncodedTemperature]], columns = ["Wether","Temperature"])

    Result = model.predict(TestPoint)
    ResultLabel = PlayLE.inverse_transform(Result)[0]

    print("Wether :",TestWether," Temperature :",TestTemperature)
    print("Predicted Result (Play) :",ResultLabel)
    print(border)

    # Step 5 : Calculate Accuracy
    CheckAccuracy(X,Y)

##################################################
#
#  Main
#
##################################################

def main():
    MarvellousClassifier("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()
