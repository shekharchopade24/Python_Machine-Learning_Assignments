

def Add(Value1, Value2):
    return Value1 + Value2  


def main():
    Value1= int(input("Enter the first value: "))
    Value2= int(input("Enter the second value: "))

    result = Add(Value1, Value2)

    print("Addition is:", result)

if __name__ == "__main__":
    main()