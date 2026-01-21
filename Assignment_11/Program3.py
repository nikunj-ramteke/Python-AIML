def SumDigit(No):
    Sum = 0
    Rem = 0
    while(No > 0):
        Rem = No % 10
        No = No // 10
        Sum = Sum + Rem

    return Sum

def main():
    No = int(input("Enter a number : "))

    Ret = SumDigit(No)

    print(Ret)
    
if _name_ == "_main_":
    main()
