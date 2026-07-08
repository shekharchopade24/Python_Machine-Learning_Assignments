 
from functools import reduce


Ret = lambda x, y: x + y
def main():
    Value = int(input("Enter a number of elements: "))
    Data = []
    for i in range(Value):
        Element = int(input("Enter element: "))
        Data.append(Element)
    print("List of elements:", Data)


    Result = reduce(Ret,Data)
    print("Result:", Result)


if __name__ == "__main__":
    main()