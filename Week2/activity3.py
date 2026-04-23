# Define Calculator class
class Calculator:
    # Set the data of class
    def set_data(self, x, y):
        self.x = x
        self.y = y
    
    # Calculate sum of member variables
    def calc_sum(self):
        return self.x + self.y;

    # Calculate power of member variables
    def calc_power(self):
        return self.x ** self.y
    
    # Calculate sum of two specific complex value
    def calc_complex(self, x, y):
        return x + y;

# Get input and return a Calculator object
def get_input():
    try:
        x = int(input("Please enter an integer value - x: "))
        y = int(input("Please enter an integer value - y: "))

        # Create calculator object and set data
        calculator = Calculator()
        calculator.set_data(x, y)

        return calculator;
    except ValueError:
        print("Invalid integer number!")
        raise

# Call function of calulator object and output the result
def output(calculator):
    print(f"Call calculator.calc_sum({calculator.x}, {calculator.y}), result is ", calculator.calc_sum())
    print(f"Call calculator.calc_power({calculator.x, calculator.y}), result is ", calculator.calc_power())

    # Specific complex value and call the function of calculator object
    x = 2 + 3j
    y = 4 + 2j
    print(f"Call calculator.calc_complex({x}, {y}), result is ", calculator.calc_complex(x, y))

# Define the main funtion of this program
def main():
    print("Call get_input function: ")
    try:
        calculator = get_input()
        print("Call output function")
        output(calculator)
    except:
        print("Input valid value, please try it later.")

# Main entrance of calling
if __name__ == "__main__":
    main()
