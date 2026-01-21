def DispGrade(Marks):
    if (Marks >= 75):
        print("Distinction")
    elif (Marks >= 60):
        print("First Class")
    elif (Marks >= 50):
        print("Second Class")
    elif (Marks < 50):
        print("Fail")
    

def main():
    Marks = int(input("Enter number : "))

    DispGrade(Marks)

if _name_ == "_main_":
    main()
