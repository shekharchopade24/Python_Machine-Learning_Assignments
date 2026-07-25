import sys

def main():
    Border = "-"*40
    print(Border)
    print("Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv)==2):
        try:
            fobj1 = open(sys.argv[1],"r")
            fobj2 = open("Demo.txt","w")

            Data = fobj1.read()

            fobj2.write(Data)

            print("Demo.txt Gets Created And Contents Of",sys.argv[1],"Gets Copied Into It")

            fobj1.close()
            fobj2.close()
        except FileNotFoundError as fobj3:
            print("File is not Present in the current Directory",fobj3)
    else:
        print("Invalid number of arguments")
        print("Plss use : python FileName.py ExistingFileName")

    print(Border)
    print(" Thank You For Marvellous Automation Script ")
    print(Border)

if __name__== "__main__":
    main()
