
import threading

def ChkPrime(Value):
    
    Data2 = []
    for i  in Value:
         flg = False
         for j in range(2,int(i/2)+1):
             if i % j == 0:
                flg = True
                break
         if flg == False:
            
            Data2.append(i)
    print("Prime Data :",Data2)


def ChkNonPrime(Value):
    
    Data2 = []
    for i  in Value:
         flg = False
         for j in range(2,int(i/2)+1):
             if i % j == 0:
                flg = True
                break
         if flg == True:
            
            Data2.append(i)
    print(" Non Prime Data :",Data2)
            

    

        

def main():
    Data =[21,13,2,11,17,19,80,33,10,3]

    ChkPrimeNo = threading.Thread(target=ChkPrime , args=(Data,))
    ChkPrimeNo.start()
    ChkPrimeNo.join()
    ChkNonPrimeNo = threading.Thread(target=ChkNonPrime , args=(Data,))
    ChkNonPrimeNo.start()
    ChkNonPrimeNo.join()

if __name__=="__main__":
    main()