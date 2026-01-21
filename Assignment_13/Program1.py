def CalculateArea(len,wid):
    Area = len * wid

    return Area

def main():
    len = int(input("Enter length : "))

    wid = int(input("Enter width : "))

    Ret = CalculateArea(len,wid)

    print("Area of rectangle is : ",Ret)


if _name_ == "_main_":
    main()
