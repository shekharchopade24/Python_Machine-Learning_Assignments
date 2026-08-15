import pandas as pd

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

def main():
    MarvellousClassifier("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()
