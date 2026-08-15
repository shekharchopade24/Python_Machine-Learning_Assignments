import pandas as pd

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

def main():
    MarvellousClassifier("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
    main()
