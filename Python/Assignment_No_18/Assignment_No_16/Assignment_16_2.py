def ChekNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    Value = int(input("Enter Number: "))
    ChekNum(Value)

if __name__ == "__main__":
    main()  