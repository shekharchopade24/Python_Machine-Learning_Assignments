
from Arithmatic import Add, Divide, Multiply, Subtract


def main():
    Value1 = int(input("Enter First Number: "))
    Value2 = int(input("Enter Second Number: "))

    Result1 = Add(Value1, Value2)
    print("Addition is:", Result1)

    Res2 = Subtract(Value1, Value2)
    print("Subtraction is:", Res2)

    Res3 = Multiply(Value1, Value2)
    print("Multiplication is:", Res3)
    
    Res4 = Divide(Value1, Value2)
    print("Division is:", Res4)
    

if __name__ == "__main__":
    main()  