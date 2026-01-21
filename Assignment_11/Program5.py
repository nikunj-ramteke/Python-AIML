def CheckPalindrome(No):
    Rev = 0
    Num = No
    while(Num > 0):
        Rem = Num % 10
        Rev = Rev * 10 + Rem
        Num = Num // 10

    if Rev == No:
        return True

def main():
    No = int(input("Enter a number : "))

    Ret = False

    Ret = CheckPalindrome(No)

    if Ret == True:
        print("It is palindrome")
    else:
        print("It is not palindrome")
    
if _name_ == "_main_":
    main()
