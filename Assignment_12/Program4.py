def PrintNum(No):
    for i in range(1,No+1):
        print(i,end=" ")

def main():
    No = int(input("Enter first number : "))

    PrintNum(No)

if _name_ == "_main_":
    main()
