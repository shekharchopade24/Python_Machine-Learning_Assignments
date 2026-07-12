from multiprocessing import Pool, current_process

def IsPrime(iNum):
    if iNum < 2:
        return False
    for iDiv in range(2, int(iNum ** 0.5) + 1):
        if iNum % iDiv == 0:
            return False
    return True

def CountPrimes(iN):
    iCount = 0
    for iNum in range(2, iN + 1):
        if IsPrime(iNum):
            iCount += 1
    print("Process ID :", current_process().pid)
    print("Input Number :", iN)
    print("Prime Count :", iCount)
    return iCount

def main():
    Data = [10000, 20000, 30000, 40000]
    with Pool() as ObjPool:
        ObjPool.map(CountPrimes, Data)

if __name__ == "__main__":
    main()
