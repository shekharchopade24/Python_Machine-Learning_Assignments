def main():

    try:
        FirstFile = input("Enter Name Of Existing File : ")
        SecondFile = input("Enter Name Of New File : ")

        fobj1 = open(FirstFile,"r")
        fobj2 = open(SecondFile,"w")

        Data = fobj1.read()

        fobj2.write(Data)

        print("Contents Of",FirstFile,"Gets Copied Into",SecondFile)

        fobj1.close()
        fobj2.close()
    except FileNotFoundError as fobj3:
        print("File is not Present in the current Directory",fobj3)

if __name__=="__main__":
    main()
