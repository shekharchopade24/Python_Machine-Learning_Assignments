from multiprocessing import Pool, current_process

def CountOddNumbers(iN):
    iCount = (iN + 1) // 2
    print("Process ID :", current_process().pid)
    print("Input Number :", iN)
    print("Odd Number Count :", iCount)
    return iCount

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    with Pool() as ObjPool:
        ObjPool.map(CountOddNumbers, Data)

if __name__ == "__main__":
    main()
