
Ret = lambda x: (x * x)
def main():
    Data = [5,6,7,8,9,10]

    Result = list(map(Ret, Data))
    print(Result)

if __name__ == "__main__":
    main() 