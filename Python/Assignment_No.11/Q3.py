
def SumOfDigits(No):

    Sum = 0

    while(No > 0):

        Digit = No % 10

        Sum = Sum + Digit

        No = No // 10

    print(Sum)

def main():

    iValue = int(input("Enter Number :"))

    SumOfDigits(iValue)

if __name__ == "__main__":

    main()