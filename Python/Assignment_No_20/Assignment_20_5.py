import threading


def GetOneTo():
    for i in range(1,50+1):
        print(i,end="  ")
        
    print()
    print("Name :",threading.current_thread().name)
    print("ID :",threading.get_ident())
  
   
   
  


def GetRev():
      for i in range(50,0,-1):

        print(i,end=" ")

      print()
      print("Name :",threading.current_thread().name)
      print("Id",threading.get_ident())



def main():
   
    GetSeq = threading.Thread(target=GetOneTo)
    GetSeq.start()
    GetSeq.join()

    
    
    GetRev1 = threading.Thread(target=GetRev)
    GetRev1.start()
    GetRev1.join

    print("Exit From Main")
    

if __name__=="__main__":
    main()