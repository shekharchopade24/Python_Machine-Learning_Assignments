def ChkPrime(No):
    if No > 1:
        for i in range(2, int(No / 2) + 1):
            if No % i == 0:
                return False
        return True
    else:
        return False