class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self, iAmount):
        self.Amount += iAmount
        print("Amount Deposited :", iAmount)

    def Withdraw(self, iAmount):
        if iAmount > self.Amount:
            print("Insufficient balance for withdrawal")
        else:
            self.Amount -= iAmount
            print("Amount Withdrawn :", iAmount)

    def CalculateInterest(self):
        fInterest = (self.Amount * BankAccount.ROI) / 100
        return fInterest

def main():
    Obj1 = BankAccount("Ajay", 5000)
    Obj1.Display()
    Obj1.Deposit(2000)
    Obj1.Withdraw(1000)
    print("Interest :", Obj1.CalculateInterest())
    Obj1.Display()

    Obj2 = BankAccount("Sanjay", 10000)
    Obj2.Display()
    Obj2.Withdraw(15000)
    print("Interest :", Obj2.CalculateInterest())

if __name__ == "__main__":
    main()
