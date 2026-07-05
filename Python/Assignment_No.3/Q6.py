import sys

no = int(input("Enter the Number :"))
print("Type is:",type(no))
print("Memory address is : ",id(no))
print("Size is :",sys.getsizeof(no))