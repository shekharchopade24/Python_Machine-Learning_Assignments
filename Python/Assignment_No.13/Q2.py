
def CircleArea(Radius):

    Area = 3.14159 * Radius * Radius

    print(Area)

def main():

    iRadius = float(input("Enter Radius :"))

    CircleArea(iRadius)

if __name__ == "__main__":

    main()