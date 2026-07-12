import time
from multiprocessing import Pool, current_process

def SumOfFifthPowers(iN):
    iSum = 0
    for iNum in range(1, iN + 1):
        iSum += iNum ** 5
    print("Process ID :", current_process().pid)
    print("Input Number :", iN)
    print("Sum of Fifth Powers :", iSum)
    return iSum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    fStartTime = time.time()

    with Pool() as ObjPool:
        ObjPool.map(SumOfFifthPowers, Data)

    fEndTime = time.time()

    print("Total Execution Time :", fEndTime - fStartTime, "seconds")

if __name__ == "__main__":
    main()
