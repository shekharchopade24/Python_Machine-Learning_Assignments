
Ret = lambda x,y: x if x < y else y
def main():
    Value1 = int(input("Enter the first number: "))
    Value2 = int(input("Enter the second number: "))    
    Result = Ret(Value1, Value2)
    print(f"The Minimum Of {Value1} and {Value2} is {Result}")
if __name__ == "__main__":
    main()  