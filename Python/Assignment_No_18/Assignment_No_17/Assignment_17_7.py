


def main():
    Value = int(input("Input :"))
    for i in range(1,Value+1):
        for j  in range(1,Value+1):
            print(j ,end="   ")
        print(" ")

if __name__=="__main__":
    main()