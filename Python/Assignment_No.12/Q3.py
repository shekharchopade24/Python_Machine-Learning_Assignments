
def Calculate(No1, No2):

    print("Addition :", No1 + No2)

    print("Subtraction :", No1 - No2)

    print("Multiplication :", No1 * No2)

    print("Division :", No1 / No2)

def main():

    iValue1 = int(input("Enter First Number :"))

    iValue2 = int(input("Enter Second Number :"))

    Calculate(iValue1, iValue2)

if __name__ == "__main__":

    main()
