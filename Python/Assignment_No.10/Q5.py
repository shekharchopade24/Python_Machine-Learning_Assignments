def OddNumber(No):
    i = 0
    for i in range(1 ,No+1):
        if(i%2 == 1):
            print(i)

def main():
    iValue = int(input("Enter Number to get Odd :"))

    OddNumber(iValue)
    
if __name__  == "__main__":
    main()