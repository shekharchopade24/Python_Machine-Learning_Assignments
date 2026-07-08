from functools import reduce

from MarvelousNum import ChkPrime


Ret = lambda x, y: (x + y)

def main():
    Value = int(input("Enter number of elements: "))
    Data = []   
    for i in range(Value):
        Element = int(input("Enter element: "))
        Data.append(Element)
    print("List of elements:", Data)

    PrimeNo =list(filter(ChkPrime,Data))

    print("List of Prime Numbers:", PrimeNo)

    result = reduce(Ret, PrimeNo)

    print("Sum of Prime Numbers:", result)


if __name__ == "__main__":
    main()