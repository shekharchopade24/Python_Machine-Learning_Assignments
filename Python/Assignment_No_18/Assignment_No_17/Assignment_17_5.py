
def PrimeNO(No):
    Flg = False
    for i in range(2,int(No/2)+1):
        if No % i == 0 :

            Flg = True
            break
        else:
            Flg = False

    return Flg

def main():
    Value = int(input("Input :"))
    Result = PrimeNO(Value)

    if Result == True :
        print(f"{Value} is  not a prime no")

    else:
        print(f"{Value} Is A Prime Number ")

if __name__ == "__main__":
    main()

    
