def positiveNegative(no):
    if no>0:
        print("this is positive number")
    elif no<0:
        print("this is negative number")
    else:
        print("this is zero")
    

def main():

    number=int((input("Enter the number:")))
    positiveNegative(number)
if __name__ =="__main__":
    main()