
def PerfectNumberCheck(No):

    Sum = 0

    for i in range(1, No):

        if(No % i == 0):

            Sum = Sum + i

    if(Sum == No):

        print("Perfect Number")

    else:

        print("Not Perfect Number")

def main():

    iValue = int(input("Enter Number :"))

    PerfectNumberCheck(iValue)

if __name__ == "__main__":

    main()
