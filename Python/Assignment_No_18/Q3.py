 
from functools import reduce


def Ret(x, y):
    if x < y:
        return x
    else:
        return y

def main():
    Value = int(input("Enter a number of elements: "))
    Data = []
    for i in range(Value):
        Element = int(input("Enter element: "))
        Data.append(Element)
    print("List of elements:", Data)


    Result = reduce(Ret,Data)
    print("Minimum Number Of Element:", Result)


if __name__ == "__main__":
    main()