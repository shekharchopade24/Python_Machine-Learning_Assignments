Ret = lambda no: no % 5 == 0

def main():
    no1 = int(input("Enter a number: "))
    result = Ret(no1)

    print(result)
if __name__ =="__main__":
    main()