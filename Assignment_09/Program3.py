def NumSquare(No):
    Sq = 1
    Sq = No * No
    return Sq

def main():
    No = int(input("Enter a number : "))

    Ret = NumSquare(No)
    
    print(Ret)

if _name_ == "_main_":
    main()
