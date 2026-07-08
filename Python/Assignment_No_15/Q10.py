
Ret = lambda x: (x % 2 == 0)
def main():
    Data = [23,1,44,34,4,7,9]

    Result = list(filter(Ret, Data))
    print("Total Number Of Even Numbers:", len(Result))

if __name__ == "__main__":
    main()