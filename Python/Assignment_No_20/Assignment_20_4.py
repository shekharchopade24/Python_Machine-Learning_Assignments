import threading


def IsUpper(Ch):
    cnt = 0
    for i in Ch:
        if i.isupper():
            cnt = cnt+1
        
    print("Upper Case Char :",cnt)
    print("Is_Upper Case Tread Name",threading.current_thread().name)
    print("Id Of Is_Upper Case Thread Id :",threading.get_ident())
   
   
   
  


def IsLower(Ch):
    cnt = 0
    for i in Ch:
        if i.islower():
            cnt = cnt+1
        
    print("Lower Case Char :",cnt)
    print("Is_Lower Case Tread Name",threading.current_thread().name)
    print("Id Of Is_Lower Case Thread Id :",threading.get_ident())


def IsDigit(Ch):
    cnt = 0
    for i in Ch:
        if i.isdigit():
            cnt = cnt+1
        
    print("Digit :",cnt)
    print("Digit Tread Name",threading.current_thread().name)
    print("Id Of Digit Thread Id :",threading.get_ident())

    
    

   
     
        


def main():
    Str1 = "ShubhamTur2626"
    ChkUpper = threading.Thread(target=IsUpper, args=(Str1,))
    ChkUpper.start()

    ChkUpper.join()
    
    ChkLower = threading.Thread(target=IsLower, args= (Str1,))
    ChkLower.start()
    ChkLower.join()

    ChkDigit = threading.Thread(target=IsDigit, args= (Str1,))
    ChkDigit.start()
    ChkDigit.join()

    print("Exit From Main")
    print("Main Tread Name",threading.current_thread().name)
    print("Id Of Main Thread Id :",threading.get_ident())
    

if __name__=="__main__":
    main()