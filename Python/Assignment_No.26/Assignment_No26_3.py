class Arithmetic:
    def __init__(self):
        self.iValue1 = 0
        self.iValue2 = 0

    def Accept(self):
        self.iValue1 = int(input("Enter Value1 : "))
        self.iValue2 = int(input("Enter Value2 : "))

    def Addition(self):
        return self.iValue1 + self.iValue2

    def Subtraction(self):
        return self.iValue1 - self.iValue2

    def Multiplication(self):
        return self.iValue1 * self.iValue2

    def Division(self):
        if self.iValue2 == 0:
            print("Error : Division by zero is not allowed")
            return None
        return self.iValue1 / self.iValue2

def main():
    iNoOfObjects = int(input("Enter number of objects : "))

    ObjList = []
    for i in range(iNoOfObjects):
        Obj = Arithmetic()
        Obj.Accept()
        ObjList.append(Obj)

    for Obj in ObjList:
        print("Addition :", Obj.Addition())
        print("Subtraction :", Obj.Subtraction())
        print("Multiplication :", Obj.Multiplication())
        print("Division :", Obj.Division())

if __name__ == "__main__":
    main()
