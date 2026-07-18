class Circle:
    PI = 3.14

    def __init__(self):
        self.fRadius = 0.0
        self.fArea = 0.0
        self.fCircumference = 0.0

    def Accept(self):
        self.fRadius = float(input("Enter Radius of Circle : "))

    def CalculateArea(self):
        self.fArea = Circle.PI * self.fRadius * self.fRadius

    def CalculateCircumference(self):
        self.fCircumference = 2 * Circle.PI * self.fRadius

    def Display(self):
        print("Radius :", self.fRadius)
        print("Area :", self.fArea)
        print("Circumference :", self.fCircumference)

def main():
    iNoOfCircles = int(input("Enter number of circles : "))

    ObjList = []
    for i in range(iNoOfCircles):
        Obj = Circle()
        Obj.Accept()
        Obj.CalculateArea()
        Obj.CalculateCircumference()
        ObjList.append(Obj)

    for Obj in ObjList:
        Obj.Display()

if __name__ == "__main__":
    main()
