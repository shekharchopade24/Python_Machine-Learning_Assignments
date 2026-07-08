Ret = lambda x:  (x % 5 == 0)

def main():
    Value1 = int(input("Enter  number: "))
    Result = Ret(Value1)
    print(Result)

if __name__ == "__main__":
    main()  