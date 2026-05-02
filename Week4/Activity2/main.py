from rect_land import RectLand

def get_data():
    try:
        length = float(input("Please enter the length of rectangular land: "))
        width = float(input("Please enter the width of rectangular land: "))
        
        return RectLand(length, width)
    except ValueError:
        print("Invalid enter value!")

def calc_result(rectland):
    print("The area of rectangular land is:", rectland.calc_area())
    print("The perimeter of rectangular land is:", rectland.calc_perimeter())

def main():
    rectland = get_data()
    if (rectland):
        calc_result(rectland)

if __name__ == "__main__":
    main()
