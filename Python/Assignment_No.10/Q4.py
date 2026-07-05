def NaturalNumber(No):
    for i in range(1 ,No+1 ,2):
        return i


def main():
    iValue = int(input("Enter Number to get Factorial :"))
    Ret = 0

    Ret = NaturalNumber(iValue)
    
    print(Ret)
    
if __name__  == "__main__":
    main()