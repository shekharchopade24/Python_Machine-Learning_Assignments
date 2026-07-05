def CountDigits(No):

    Count = 0

    while(No > 0):

        No = No // 10

        Count = Count + 1

    print(Count)

def main():

    iValue = int(input("Enter Number :"))

    CountDigits(iValue)

if __name__ == "__main__":

    main()