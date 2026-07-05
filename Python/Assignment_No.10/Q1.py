def Mult(No):
    Count = 1
    while(Count <= 10):
        print(Count * No)
        Count = Count + 1
    return No


def main():
    iValue = int(input("Enter Number to get Multiplication table :"))

    Mult(iValue)
    
if __name__  == "__main__":
    main()