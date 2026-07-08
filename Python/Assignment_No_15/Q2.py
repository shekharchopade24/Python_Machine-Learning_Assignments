Ret = lambda x : (x % 2 == 0) 

def main():
    Value = [5,1,6,7,8,9,2]

    Result = list(filter(Ret,Value))

    print(Result)

    

if __name__ == "__main__":
    main()  
