def CheckPrime(No):
    for i in range(2,No):
        if No % i == 0 :
            return False
        else:
            return True

def main():
    No = int(input("Enter a number : "))

    Ret = CheckPrime(No)

    if Ret == True:
        print("it is prime")
    else:
        print("it is not prime")
    
if _name_ == "_main_":
    main()
