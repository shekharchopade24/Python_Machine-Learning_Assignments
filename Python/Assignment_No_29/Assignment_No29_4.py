import sys

def main():
    Border = "-"*40
    print(Border)
    print("Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv)==3):
        try:
            fobj1 = open(sys.argv[1],"r")
            fobj2 = open(sys.argv[2],"r")

            Data1 = fobj1.read()
            Data2 = fobj2.read()

            if(Data1 == Data2):
                print("Success")
            else:
                print("Failure")

            fobj1.close()
            fobj2.close()
        except FileNotFoundError as fobj3:
            print("File is not Present in the current Directory",fobj3)
    else:
        print("Invalid number of arguments")
        print("Plss use : python FileName.py FirstFile SecondFile")

    print(Border)
    print(" Thank You For Marvellous Automation Script ")
    print(Border)

if __name__== "__main__":
    main()
