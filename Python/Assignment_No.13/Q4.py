def BinaryEquivalent(No):

    Binary = ""

    if(No == 0):

        Binary = "0"

    while(No > 0):

        Rem = No % 2

        Binary = str(Rem) + Binary

        No = No // 2

    print(Binary)

def main():

    iValue = int(input("Enter Number :"))

    BinaryEquivalent(iValue)

if __name__ == "__main__":

    main()