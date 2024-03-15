def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

def main():
        for  in range(5):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            operator = input("Enter the operator (+, -, *, /): ")

            if operator not in ("+", "-", "*", "/"):
                raise ValueError("Invalid operator!")

            result = calculate(num1, num2, operator)

            user_answer = float(input("Enter your answer: "))

            if result == user_answer:
                print("Correct!")
            else:
                print("Wrong!")

            print()  # Add a newline for better readability

        except ValueError as e:
            print("Error:", str(e))
            print("Please enter valid numbers and operator.")
            print()
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            print("Please enter a non-zero denominator.")
            print()
        except Exception as e:
            print("An error occurred:", str(e))
            print("Please try again.")
            print()

if __name__ == '__main__':
    main()