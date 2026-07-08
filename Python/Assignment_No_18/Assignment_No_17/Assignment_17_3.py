def Ret(Value):
   Fact = 1
   for i in range(1, Value + 1):
         Fact = Fact * i
   return Fact
def main():
    Value = int(input("Input :"))

    Result = Ret(Value)
    print("Result is:", Result)


if __name__ == "__main__":
    main()