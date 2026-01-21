def Factors(No):
    for i in range(1,No+1):
        if (No % i == 0):
            print(i,end=" ")

def main():
    No = int(input("Enter number : "))

    Factors(No)

if _name_ == "_main_":
    main()
