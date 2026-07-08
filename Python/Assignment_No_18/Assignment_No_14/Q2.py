Ret = lambda x: x ** x

def main():
    Value = int(input("Enter a number: "))
    Result = Ret(Value) 

    print(f"The Cube Of {Value} is {Result}")


   
   
if __name__ == "__main__":
    main()