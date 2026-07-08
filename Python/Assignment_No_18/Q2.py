 
from functools import reduce


Ret = lambda x, y: x if x > y else y
def main():
    Value = int(input("Enter a number of elements: "))
    Data = []
    for i in range(Value):
        Element = int(input("Enter element: "))
        Data.append(Element)
    print("List of elements:", Data)


    Result = reduce(Ret,Data)
    print("Maximum Number Of Element:", Result)


if __name__ == "__main__":
    main()