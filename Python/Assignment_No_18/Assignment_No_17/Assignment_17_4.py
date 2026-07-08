def  FactorAdd(a):
    sum = 0
    for i in range(1,a):
        if a % i == 0:
            sum += i
    return sum      

def main():
    Value = int(input("Input :"))

    Result = FactorAdd(Value)
    print("Result is:", Result)

if __name__ == "__main__":
    main()