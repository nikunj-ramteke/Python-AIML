def PrintNum(No):
    for i in range(No,0,-1):
        print(i,end=" ")

def main():
    No = int(input("Enter first number : "))

    PrintNum(No)

if _name_ == "_main_":
    main()
