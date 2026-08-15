
def Add(no1 , no2):
    ans = no1+no2
    return ans 

    
def main():
    number1 = int(input("Enter a number: "))
    number2 = int(input("enter a number: "))
    ans = Add(number1, number2)
    
    print("The sum is:", ans)

if __name__ == "__main__":
    main()