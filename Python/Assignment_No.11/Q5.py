
def PalindromeCheck(No):

    Temp = No

    Rev = 0

    while(Temp > 0):

        Digit = Temp % 10

        Rev = (Rev * 10) + Digit

        Temp = Temp // 10

    if(No == Rev):

        print("Palindrome")

    else:

        print("Not Palindrome")

def main():

    iValue = int(input("Enter Number :"))

    PalindromeCheck(iValue)

if __name__ == "__main__":

    main()
