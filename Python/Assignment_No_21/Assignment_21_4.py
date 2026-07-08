
import threading

def ChkPrime(Value,Res):
    Sum = 0
    for i in Value:
        Sum = Sum+i
    Res.append(Sum)



    
    
    


def ChkNonPrime(Value,Res):
    Prod = 1
    for i in Value:
        Prod = Prod*i
    Res.append(Prod)

   
        
    
    
   
    

        

def main():
    Data =[21,13,2,11,17,19,80,33,10,3]
    Prod1 = []
    Sum1 =[]

    ChkPrimeNo = threading.Thread(target=ChkPrime , args=(Data,Sum1,))
    ChkPrimeNo.start()
    ChkPrimeNo.join()
    ChkNonPrimeNo = threading.Thread(target=ChkNonPrime , args=(Data,Prod1,))
    ChkNonPrimeNo.start()
    ChkNonPrimeNo.join()
    print("Summation of :",Sum1)
    print("Product Of :",Prod1)

if __name__=="__main__":
    main()