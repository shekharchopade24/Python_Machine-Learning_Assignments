


def main():
    Value = int(input("Input :"))
    for i in range(Value,0,-1):
        for j  in range(1,i+1):
            print("  * " ,end="   ")
        print(" ")

if __name__=="__main__":
    main()