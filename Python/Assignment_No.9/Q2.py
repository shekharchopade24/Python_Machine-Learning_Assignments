def GreaterNumber(No1,No2):
    if(No1 < No2):
        print(No2)
    elif(No2 < No1):
        print(No1)

def main():
    iValue1 = int(input("Enter First Number :"))
    iValue2 = int(input("Enter Second Number :"))

    GreaterNumber(iValue1,iValue2)
    
if __name__  == "__main__":
    main()