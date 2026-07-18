class Numbers:
    def __init__(self, iValue):
        self.iValue = iValue

    def ChkPrime(self):
        if self.iValue < 2:
            return False
        for iDiv in range(2, int(self.iValue ** 0.5) + 1):
            if self.iValue % iDiv == 0:
                return False
        return True

    def ChkPerfect(self):
        iSum = 0
        for iDiv in range(1, self.iValue):
            if self.iValue % iDiv == 0:
                iSum += iDiv
        return iSum == self.iValue

    def Factors(self):
        print("Factors of", self.iValue, ": ", end="")
        for iDiv in range(1, self.iValue + 1):
            if self.iValue % iDiv == 0:
                print(iDiv, end=" ")
        print()

    def SumFactors(self):
        iSum = 0
        for iDiv in range(1, self.iValue + 1):
            if self.iValue % iDiv == 0:
                iSum += iDiv
        return iSum

def main():
    Obj1 = Numbers(28)
    print("Is Prime :", Obj1.ChkPrime())
    print("Is Perfect :", Obj1.ChkPerfect())
    Obj1.Factors()
    print("Sum of Factors :", Obj1.SumFactors())

    Obj2 = Numbers(17)
    print("Is Prime :", Obj2.ChkPrime())
    print("Is Perfect :", Obj2.ChkPerfect())
    Obj2.Factors()
    print("Sum of Factors :", Obj2.SumFactors())

if __name__ == "__main__":
    main()
