
def PrimeNumber(No):

    IsPrime = True

    for i in range(2, No-1):

        if(No % i == 0):

            IsPrime = False

    if(IsPrime):

        print("Prime Number")

    else:

        print("Not Prime Number")

def main():

    iValue = int(input("Enter Number :"))

    PrimeNumber(iValue)

if __name__ == "__main__":

    main()