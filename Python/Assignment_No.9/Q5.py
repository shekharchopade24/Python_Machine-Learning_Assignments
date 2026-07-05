def DiviSibleOfThatNumber(No):
    if(No % 3 == 0 and No % 5 == 0):
       print("Divisible by 3 and 5")

def main():
    iValue = int(input("Enter Number to check the it is divisible by 3 and 5 :"))

    Ret = DiviSibleOfThatNumber(iValue)
    
    
if __name__  == "__main__":
    main()