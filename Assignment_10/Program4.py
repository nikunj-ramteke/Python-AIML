def PrintEven(No):
    for i in range(1,No+1):
        if (i % 2 == 0):
            print(i,end=" ")
    
def main():
    No = int(input("Enter a number : "))

    PrintEven(No)
    
if _name_ == "_main_":
    main()
