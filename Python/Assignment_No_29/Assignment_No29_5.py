def main():

    try:
        FileName = input("Enter File Name : ")
        Word = input("Enter String To Search : ")

        fobj = open(FileName,"r")

        Data = fobj.read()

        Words = Data.split()

        Count = 0

        for w in Words:
            if(w == Word):
                Count = Count + 1

        print("Word",Word,"Is Present",Count,"Times In File",FileName)

        fobj.close()
    except FileNotFoundError as fobj1:
        print("File is not Present in the current Directory",fobj1)

if __name__=="__main__":
    main()
