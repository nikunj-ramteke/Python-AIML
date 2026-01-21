def PrintBinary(No):
    Binary = bin(No)

    print(Binary)

def main():
    No = int(input("Enter number : "))

    PrintBinary(No)

if _name_ == "_main_":
    main()
