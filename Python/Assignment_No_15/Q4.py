
from functools import reduce


Ret = lambda x, y: x + y

def main():
    Data = [23, 45, 67, 32, 89, 90]
    Result = (reduce(Ret, Data))

    print("Addition of all elements is:", Result)

if __name__ == "__main__":
    main()