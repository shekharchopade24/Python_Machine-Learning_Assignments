def main():

    try:
        FileName = input("Enter File Name : ")

        fobj = open(FileName,"r")

        Data = fobj.read()

        Words = Data.split()

        Count = len(Words)

        print("Total Number Of Words In File Are :",Count)

        fobj.close()
    except FileNotFoundError as fobj1:
        print("File is not Present in the current Directory",fobj1)

if __name__=="__main__":
    main()
