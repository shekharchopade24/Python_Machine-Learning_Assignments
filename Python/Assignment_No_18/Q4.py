
def main():
    Value = int(input("Enter a number of elements: "))
    Data = []
    for i in range(Value):
        Element = int(input("Enter element: "))
        Data.append(Element)
    print("List of elements:", Data)

    No = int(input("Enter a number to search: "))
    Fer = Data.count(No)
    print("Frequency of", No, "is:", Fer)




if __name__ == "__main__":
    main()