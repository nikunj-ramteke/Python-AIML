def CountDigit(No):
    Count = 0
    while(No > 0):
        No = No // 10
        Count = Count + 1

    return Count

def main():
    No = int(input("Enter a number : "))

    Ret = CountDigit(No)

    print(Ret)
    
if _name_ == "_main_":
    main()
