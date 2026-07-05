
def PrintFactors(No):

    for i in range(1, No+1):

        if(No % i == 0):

            print(i, end=" ")

    print()

def main():

    iValue = int(input("Enter Number :"))

    PrintFactors(iValue)

if __name__ == "__main__":

    main()
