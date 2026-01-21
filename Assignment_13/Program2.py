def CalculateArea(radius):
    Area = 3.14 * radius *radius

    return Area

def main():
    radius = int(input("Enter radius : "))

    Ret = CalculateArea(radius)

    print("Area of circle is : ",Ret)


if _name_ == "_main_":
    main()
