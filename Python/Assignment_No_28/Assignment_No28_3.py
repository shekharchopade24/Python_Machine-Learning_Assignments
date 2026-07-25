def main():

    try:
        FileName = input("Enter File Name : ")

        fobj = open(FileName,"r")

        for Line in fobj:
            print(Line)

        fobj.close()
    except FileNotFoundError as fobj1:
        print("File is not Present in the current Directory",fobj1)

if __name__=="__main__":
    main()
