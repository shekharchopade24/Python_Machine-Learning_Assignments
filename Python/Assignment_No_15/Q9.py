

from functools import reduce
Ret = lambda x, y: x * y


def main():
    Data = [12,15,20,25,30]

    Result = reduce(Ret, Data)
    print("Product of elements in the list is:", Result)

if __name__ == "__main__":
    main()