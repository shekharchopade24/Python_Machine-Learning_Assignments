def main():

    try:
        FileName = input("Enter File Name : ")

        fobj = open(FileName,"r")

        Lines = fobj.readlines()

        Count = len(Lines)

        print("Total Number Of Lines In File Are :",Count)

        fobj.close()
    except FileNotFoundError as fobj1:
        print("File is not Present in the current Directory",fobj1)

if __name__=="__main__":
    main()
