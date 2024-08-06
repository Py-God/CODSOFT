class Calculator():

    def calculate(self, op):
        
        while True:
            try:
                no1 = int(input("First Number: "))
                no2 = int(input("Second Number: "))
            except ValueError:
                print("You have to supply two integers.")
            else:
                break

        if op == "a":
            res = no1 + no2
        elif op == "s":
            res = no1 - no2
        elif op == "d":
            res = no1 / no2
        elif op == "m":
            res = no1 * no2

        print("Result = ", res)
        print()

        
def main():
    print("Calculator")
    print("----------")
    print("Type: a - addition, s - subtraction, m - multiplication, d - division, x - exit")

    calc = Calculator()

    while True:
        operator = input("Enter an operator: ")

        if operator in ["a", "s", "m", "d"]:
            calc.calculate(operator)
        elif operator == "x":
            break


main()