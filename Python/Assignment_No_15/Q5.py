
from functools import reduce


Ret = lambda x, y: x if x > y else y
def main():
    Data = [23, 45, 99, 32, 89, 90]
    Result = (reduce(Ret, Data))

    print("Maximum of all elements is:", Result)
    
if __name__ == "__main__":
    main()