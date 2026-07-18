class Demo:
    Value = 0

    def __init__(self, iNo1, iNo2):
        self.iNo1 = iNo1
        self.iNo2 = iNo2

    def Fun(self):
        print("Value of no1 :", self.iNo1)
        print("Value of no2 :", self.iNo2)

    def Gun(self):
        print("Value of no1 :", self.iNo1)
        print("Value of no2 :", self.iNo2)

def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()
