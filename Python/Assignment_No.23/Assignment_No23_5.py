from multiprocessing import Pool, current_process

def Factorial(iN):
    iResult = 1
    for iNum in range(2, iN + 1):
        iResult *= iNum
    print("Process ID :", current_process().pid)
    print("Input Number :", iN)
    print("Factorial :", iResult)
    return iResult

def main():
    Data = [10, 15, 20, 25]
    with Pool() as ObjPool:
        ObjPool.map(Factorial, Data)

if __name__ == "__main__":
    main()
