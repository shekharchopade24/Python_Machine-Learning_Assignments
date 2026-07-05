
def PrintNumbers(No):

    for i in range(1, No+1):

        print(i, end=" ")

    print()

def main():

    iValue = int(input("Enter Number :"))

    PrintNumbers(iValue)

if __name__ == "__main__":

    main()