def CubeOfThatNumber(No):
    Ans = 0
    Ans  = No * No * No
    return Ans

def main():
    iValue = int(input("Enter Number to get Cube of that number :"))
    Ret = 0

    Ret = CubeOfThatNumber(iValue)
    
    print(Ret)
    
if __name__  == "__main__":
    main()