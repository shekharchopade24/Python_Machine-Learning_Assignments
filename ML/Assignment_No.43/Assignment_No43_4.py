import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

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

def main():
    MarvellousClassifier("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()
