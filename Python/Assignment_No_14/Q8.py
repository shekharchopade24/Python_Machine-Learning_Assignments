
Ret = lambda x, y: (x + y)

def main():
    Value1 = int(input("Enter  1st number: "))
    Value2 = int(input("Enter  2nd number: "))
    Result = Ret(Value1, Value2)
    print(f"The Addition of {Value1} and {Value2} is: {Result}")

    
if __name__ == "__main__":
    main()