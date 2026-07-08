
def Ret(Value1):
    if(Value1 > 0):
        return "Positive Number"
    elif(Value1 < 0):
        return "Negative Number"   
    else:
        return " Number is Zero"

def main():
    Value1 = int(input("Enter the first value: "))

    Retsult = Ret(Value1)
    print("Result is:", Retsult)

if __name__ == "__main__":
    main()  