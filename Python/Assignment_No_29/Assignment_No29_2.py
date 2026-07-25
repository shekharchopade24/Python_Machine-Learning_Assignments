def main():

    try:
        FileName = input("Enter File Name : ")

        fobj = open(FileName,"r")

        Data = fobj.read()

        print("Contents Of File Are :")
        print(Data)

        fobj.close()
    except FileNotFoundError as fobj1:
        print("File is not Present in the current Directory",fobj1)

if __name__=="__main__":
    main()
