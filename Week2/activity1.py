def calc_sub():
    try:
        x = int(input("Please enter integer value x: "))
        y = int(input("Please enter integer value y: "))
        print(f"The result of {x} + {y} = ", x + y)
    except ValueError:
        print("Please enter integer number!")

def calc_power():
    try:
        x = int(input("Please enter integer value x: "))
        y = int(input("Please enter integer value y: "))
        print(f"The result of power({x}, {y}) = ", x ** y)
    except ValueError:
        print("Please enter integer number!")

def calc_complex():
    x = 1 + 2j
    y = 3 + 5j
    z = x + y
    print(f"Complex number: {x} + {y} = {z}, the real of z is ", z.real, ", the imag of z is ", z.imag)

def main():
    calc_sub()
    calc_power()
    calc_complex()

if __name__ == "__main__":
    main()
