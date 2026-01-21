def NumCube(No):
    Cube = 1
    Cube = No ** 3
    return Cube

def main():
    No = int(input("Enter a number : "))

    Ret = NumCube(No)
    
    print(Ret)

if _name_ == "_main_":
    main()
