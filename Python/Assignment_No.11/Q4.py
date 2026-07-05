
def ReverseNumber(No):

    Rev = 0

    while(No > 0):

        Digit = No % 10

        Rev = (Rev * 10) + Digit

        No = No // 10

    print(Rev)

def main():

    iValue = int(input("Enter Number :"))

    ReverseNumber(iValue)

if __name__ == "__main__":

    main()