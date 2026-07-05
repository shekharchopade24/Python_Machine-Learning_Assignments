def SquareOfThatNumber(No):
    Ans = 0
    Ans  = No * No
    return Ans

def main():
    iValue = int(input("Enter Number to get square of that number :"))
    Ret = 0

    Ret = SquareOfThatNumber(iValue)
    
    print(Ret)
    
if __name__  == "__main__":
    main()