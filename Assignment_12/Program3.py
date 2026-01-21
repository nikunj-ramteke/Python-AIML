def SimpleCalc(No1,No2):
    Addition = No1 + No2
    print("Addition is ",Addition)

    Subtraction = No1 - No2
    print("Subtraction is ",Subtraction)

    Multiplication = No1 * No2
    print("Multiplication is ",Multiplication)

    Division = No1 // No2
    print("Division is ",Division)

def main():
    No1 = int(input("Enter first number : "))

    No2 = int(input("Enter first number : "))

    SimpleCalc(No1,No2)

if _name_ == "_main_":
    main()
