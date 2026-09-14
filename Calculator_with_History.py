from datetime import datetime


HISTORY_FILE = "history.txt"


def show_history():
    try:
        file = open(HISTORY_FILE, "r")
        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            print("No History Found!")
        else:
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print("No History Found!")


def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History Cleared")


def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    file.write(
        "[" + current_time + "] "
        + equation
        + " = "
        + str(result)
        + "\n"
    )

    file.close()


def show_help():
    print("\nAvailable Commands:")
    print("history       - Show calculation history")
    print("clear         - Clear calculation history")
    print("help          - Show help")
    print("exit          - Exit calculator")

    print("\nNormal Operators:")
    print("10 + 5        Addition")
    print("10 - 5        Subtraction")
    print("10 * 5        Multiplication")
    print("10 / 5        Division")
    print("10 % 3        Remainder")
    print("10 // 3       Floor division")
    print("2 ** 3        Power")


def format_result(result):
    if isinstance(result, float) and result.is_integer():
        return int(result)

    return result


def calculate(user_input):
    parts = user_input.split()

    try:
        if len(parts) != 3:
            print("Invalid input.")
            print("Use: number operator number")
            print("Example: 10 + 20")
            return

        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero")
                return

            result = num1 / num2

        elif operator == "%":
            if num2 == 0:
                print("Cannot use zero as the divisor")
                return

            result = num1 % num2

        elif operator == "//":
            if num2 == 0:
                print("Cannot divide by zero")
                return

            result = num1 // num2

        elif operator == "**":
            result = num1 ** num2

        else:
            print("Invalid operator")
            return

        result = format_result(result)

        print("Result:", result)
        save_to_history(user_input, result)

    except ValueError:
        print("Invalid number. Please enter valid numbers.")

    except OverflowError:
        print("The result is too large.")

    except Exception as error:
        print("Something went wrong:", error)


def main():
    print("WELCOME TO THE SIMPLE CALCULATOR")
    print("Type 'help' to see all commands.")

    while True:
        user_input = input(
            "\nEnter calculation or command: "
        ).strip()

        if user_input.lower() == "exit":
            print("GOODBYE!")
            break

        elif user_input.lower() == "history":
            show_history()

        elif user_input.lower() == "clear":
            clear_history()

        elif user_input.lower() == "help":
            show_help()

        elif user_input == "":
            print("Please enter something.")

        else:
            calculate(user_input)


main()