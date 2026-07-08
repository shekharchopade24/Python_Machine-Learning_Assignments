
Ret = lambda x: (x % 5 == 0) and (x % 3 == 0)
def main():
    Data = [12,15,20,25,30]

    Result = list(filter(Ret, Data))
    print(Result)


if __name__ == "__main__":
    main()