def CheckPerfect(No):
    Divisors = 0
    for i in range(1,(No//2)+1):
        if(No % i == 0):
            Divisors = Divisors + i

    if Divisors == No:
        return True

def main():
    No = int(input("Enter number : "))

    Ret = CheckPerfect(No)

    if Ret == True :
        print("It is perfect")
    else:
        print("It is not perfect")

if _name_ == "_main_":
    main()
