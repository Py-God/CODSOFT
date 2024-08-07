class Calculator():

    def calculate(self, op):
        # get the two numbers to perform operation on
        while True:
            try:
                no1 = int(input("First Number: "))
                no2 = int(input("Second Number: "))
            except ValueError:
                print("You have to supply two integers.")
                print()
            else:
                break
        
        # perform operation and return result
        if op == "a":
            res = no1 + no2
        elif op == "s":
            res = no1 - no2
        elif op == "d":
            res = no1 / no2
        elif op == "m":
            res = no1 * no2

        return res

        
def main():
    # display basic information
    print("Calculator")
    print("----------")
    print("Type: a - addition, s - subtraction, m - multiplication, d - division, x - exit")

    # create calculator object
    calc = Calculator()

    # prompt for a desired operator to use
    while True:
        operator = input("Enter an operator: ")

        if operator in ["a", "s", "m", "d"]:
            print("Result = ", calc.calculate(operator))
            print()
        elif operator == "x":
            break
        else:
            print("Invalid input")
            print()


main()