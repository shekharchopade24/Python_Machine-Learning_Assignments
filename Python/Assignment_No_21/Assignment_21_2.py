
import threading

def MaxEle(Value):
    Data = max(Value)
    print("Minimum Element  Of The List :",Data)

    
    
    

def MinEle(Value):
    Data = min(Value)
    print("Minimum Element  Of The List :",Data)
    
    

    

        

def main():
    Data =[]
    No = int(input("Enter How Many elements in List :"))
    for i in range(No):
        Value = int(input("Enter Data :"))
        Data.append(Value)

        
   

    ChkPrimeNo = threading.Thread(target=MaxEle , args=(Data,))
    ChkPrimeNo.start()
    ChkPrimeNo.join()
    ChkNonPrimeNo = threading.Thread(target=MinEle , args=(Data,))
    ChkNonPrimeNo.start()
    ChkNonPrimeNo.join()

if __name__=="__main__":
    main()