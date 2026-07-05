
def RectangleArea(Length, Width):

    Area = Length * Width

    print(Area)

def main():

    iLength = float(input("Enter Length :"))

    iWidth = float(input("Enter Width :"))

    RectangleArea(iLength, iWidth)

if __name__ == "__main__":

    main()