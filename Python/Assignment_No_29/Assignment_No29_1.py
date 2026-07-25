import os

def main():
    FileName = input("Enter File Name : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print("File",FileName,"Is Present In Current Directory")
    else:
        print("File",FileName,"Is Not Present In Current Directory")

if __name__=="__main__":
    main()
