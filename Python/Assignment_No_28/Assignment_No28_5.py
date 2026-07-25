def main():

    try:
        FileName = input("Enter File Name : ")
        Word = input("Enter Word To Search : ")

        fobj = open(FileName,"r")

        Data = fobj.read()

        if(Word in Data):
            print("Word",Word,"Is Present In File",FileName)
        else:
            print("Word",Word,"Is Not Present In File",FileName)

        fobj.close()
    except FileNotFoundError as fobj1:
        print("File is not Present in the current Directory",fobj1)

if __name__=="__main__":
    main()
