from multiprocessing import Pool, current_process

def SumOfOddNumbers(iN):
    iSum = 0
    for iNum in range(1, iN + 1, 2):
        iSum += iNum
    print("Process ID :", current_process().pid)
    print("Input Number :", iN)
    print("Sum of Odd Numbers :", iSum)
    return iSum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    with Pool() as ObjPool:
        ObjPool.map(SumOfOddNumbers, Data)

if __name__ == "__main__":
    main()
