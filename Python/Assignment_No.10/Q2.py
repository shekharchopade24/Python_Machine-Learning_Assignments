def NaturalNumber(No):
    Sum = 0
    for i in range(1 ,No+1):
        Sum = Sum + i
    return Sum


def main():
    iValue = int(input("Enter Number to get Multiplication table :"))
    Ret = 0

    Ret = NaturalNumber(iValue)
    
    print(Ret)
    
if __name__  == "__main__":
    main()