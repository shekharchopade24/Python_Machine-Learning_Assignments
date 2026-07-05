
def PrintReverse(No):

    for i in range(No, 0, -1):

        print(i, end=" ")

    print()

def main():

    iValue = int(input("Enter Number :"))

    PrintReverse(iValue)

if __name__ == "__main__":

    main()