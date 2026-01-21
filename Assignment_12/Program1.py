def CheckChar(ch):
    if (ch == "a" or ch == "e" or ch == 'i' or ch == "o" or ch == "u"):
        print("It is vowel")
    else:
        print("It is consonant")

def main():
    ch = input("Enter character : ")[0]

    CheckChar(ch)

if _name_ == "_main_":
    main()
