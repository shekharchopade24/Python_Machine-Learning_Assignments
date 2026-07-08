
Ret = lambda x, y, z: max(x, y, z)


def main():
    Value1 = int(input("Enter  1st number: "))
    Value2 = int(input("Enter  2nd number: "))
    Value3 = int(input("Enter  3rd number: "))
    Result = Ret(Value1, Value2, Value3)
    print(f"The Maximum of {Value1}, {Value2} and {Value3} is: {Result}")


if __name__ == "__main__":
    main()