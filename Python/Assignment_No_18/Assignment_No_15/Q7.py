
Ret = lambda x: (len(x) >= 5)

def main():

    Data = ['shubham','Ajay','Rohit','Sagar','Ram','Sure','Ra']

    Result = list(filter(Ret, Data))
    print(Result)

if __name__ == "__main__":
    main()

