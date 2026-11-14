
# ==================================================
#              FRANEJ AI CHATBOT
#                  VERSION 3.2
# ==================================================

import datetime
import ast
import operator
import math
import re

BOT_NAME = "FRANEJ"
VERSION = "3.2"


# ==================================================
# 1. SAFE MATHEMATICS CALCULATOR
# ==================================================

OPERATIONS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow
}


def calculate(expression, x_value=None):

    expression = expression.replace("^", "**")
    expression = re.sub(r"(\d)(x)", r"\1*\2", expression, flags=re.I)
    expression = re.sub(r"(x)(\d)", r"\1*\2", expression, flags=re.I)

    tree = ast.parse(expression, mode="eval")

    def solve(node):

        if isinstance(node, ast.Constant):
            if type(node.value) in (int, float):
                return node.value
            raise ValueError("Invalid number")

        elif isinstance(node, ast.Name):
            if node.id.lower() == "x" and x_value is not None:
                return x_value
            raise ValueError("Unknown variable")

        elif isinstance(node, ast.BinOp):

            op = type(node.op)

            if op not in OPERATIONS:
                raise ValueError("Unsupported operation")

            left = solve(node.left)
            right = solve(node.right)

            if op == ast.Div and right == 0:
                raise ZeroDivisionError

            if op == ast.Pow and abs(right) > 10:
                raise ValueError("Exponent too large")

            return OPERATIONS[op](left, right)

        elif isinstance(node, ast.UnaryOp):

            if isinstance(node.op, ast.USub):
                return -solve(node.operand)

            if isinstance(node.op, ast.UAdd):
                return solve(node.operand)

        raise ValueError("Invalid expression")

    return solve(tree.body)


# ==================================================
# 2. TIME AND DATE SYSTEM
# ==================================================

def time_system():

    now = datetime.datetime.now().astimezone()

    print("FRANEJ: Current time:", now.strftime("%I:%M %p"))
    print("FRANEJ: Today's date:", now.strftime("%B %d, %Y"))
    print("FRANEJ: Today is", now.strftime("%A"))


# ==================================================
# 3. ALGEBRAIC EQUATION SOLVER
# ==================================================

def solve_linear():

    print("\nFRANEJ ALGEBRA ENGINE")
    equation = input("Enter equation (example: 2x+5=15): ")

    try:

        if equation.count("=") != 1:
            raise ValueError("Enter one equation.")

        left, right = equation.split("=")

        a0 = calculate(left, 0) - calculate(right, 0)
        a1 = calculate(left, 1) - calculate(right, 1)
        a2 = calculate(left, 2) - calculate(right, 2)

        coefficient = a1 - a0

        if not math.isclose(a2 - a0, 2 * coefficient):
            print("FRANEJ: This is not a linear equation.")
            return

        if math.isclose(coefficient, 0):
            if math.isclose(a0, 0):
                print("FRANEJ: Infinitely many solutions.")
            else:
                print("FRANEJ: No solution.")
            return

        answer = -a0 / coefficient

        print("\nFRANEJ SOLUTION")
        print("Equation:", equation)
        print("Step 1: Collect like terms.")
        print("Step 2: Isolate x.")
        print("Step 3: Divide by the coefficient of x.")
        print("Final answer: x =", answer)

    except ZeroDivisionError:
        print("FRANEJ: Division by zero is not allowed.")

    except Exception as error:
        print("FRANEJ: Unable to solve this equation.", error)


# ==================================================
# 4. QUADRATIC EQUATION SOLVER
# ==================================================

def quadratic_solver():

    print("\nFRANEJ QUADRATIC EQUATION ENGINE")

    try:

        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("FRANEJ: This is not a quadratic equation.")
            return

        discriminant = b**2 - 4*a*c

        print("Discriminant =", discriminant)

        if discriminant > 0:

            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)

            print("Two distinct real roots:")
            print("x1 =", x1)
            print("x2 =", x2)

        elif discriminant == 0:

            x = -b / (2*a)
            print("Two equal real roots:")
            print("x =", x)

        else:

            real = -b / (2*a)
            imaginary = math.sqrt(-discriminant) / abs(2*a)

            print("Two complex roots:")
            print("x1 =", complex(real, imaginary))
            print("x2 =", complex(real, -imaginary))

    except ValueError:
        print("FRANEJ: Please enter valid numbers.")


# ==================================================
# 5. POLYNOMIAL ENGINE
# ==================================================

def polynomial_engine():

    print("\nFRANEJ POLYNOMIAL ENGINE")
    print("Enter coefficients from highest power to constant.")
    print("Example: 2, 3, 1 represents 2x^2 + 3x + 1")

    try:

        coefficients = [
            float(value.strip())
            for value in input("Coefficients: ").split(",")
        ]

        x = float(input("Enter value of x: "))

        result = 0

        for coefficient in coefficients:
            result = result * x + coefficient

        print("Polynomial value =", result)

    except ValueError:
        print("FRANEJ: Invalid polynomial input.")


# ==================================================
# 6. PHYSICS ENGINE
# ==================================================

def physics_engine():

    print("\nFRANEJ PHYSICS ENGINE")
    print("1. Work")
    print("2. Power")
    print("3. Kinetic Energy")
    print("4. Potential Energy")
    print("5. Force")
    print("6. Momentum")

    choice = input("Choose a calculation: ")

    try:

        if choice == "1":

            force = float(input("Enter force (N): "))
            distance = float(input("Enter distance (m): "))

            answer = force * distance

            print("Formula: Work = Force x Distance")
            print("Answer:", answer, "Joules")

        elif choice == "2":

            work = float(input("Enter work (J): "))
            time = float(input("Enter time (s): "))

            if time == 0:
                print("Time cannot be zero.")
                return

            answer = work / time

            print("Formula: Power = Work / Time")
            print("Answer:", answer, "Watts")

        elif choice == "3":

            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))

            answer = 0.5 * mass * velocity**2

            print("Formula: KE = 1/2 mv²")
            print("Answer:", answer, "Joules")

        elif choice == "4":

            mass = float(input("Enter mass (kg): "))
            gravity = float(input("Enter gravity (m/s²): "))
            height = float(input("Enter height (m): "))

            answer = mass * gravity * height

            print("Formula: PE = mgh")
            print("Answer:", answer, "Joules")

        elif choice == "5":

            mass = float(input("Enter mass (kg): "))
            acceleration = float(input("Enter acceleration (m/s²): "))

            answer = mass * acceleration

            print("Formula: Force = Mass x Acceleration")
            print("Answer:", answer, "Newtons")

        elif choice == "6":

            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))

            answer = mass * velocity

            print("Formula: Momentum = Mass x Velocity")
            print("Answer:", answer, "kg m/s")

        else:

            print("FRANEJ: Invalid physics selection.")

    except ValueError:
        print("FRANEJ: Please enter valid numerical values.")


# ==================================================
# 7. BASIC CHAT RESPONSE ENGINE
# ==================================================

def franej_response(message):

    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hello! Welcome to FRANEJ."

    elif "your name" in message:
        return "My name is FRANEJ."

    elif "who created you" in message:
        return "I was created by my developer."

    elif "how are you" in message:
        return "I am functioning properly. How can I help?"

    elif "what can you do" in message:
        return "I can assist with mathematics, physics, time and date."

    elif "thank you" in message:
        return "You are welcome!"

    elif "time" in message or "date" in message or "day" in message:
        now = datetime.datetime.now().astimezone()
        return (
            "Time: " + now.strftime("%I:%M %p") +
            "\nDate: " + now.strftime("%B %d, %Y") +
            "\nDay: " + now.strftime("%A")
        )

    elif message.startswith("calculate "):

        try:
            expression = message.replace("calculate ", "", 1)
            return "The answer is " + str(calculate(expression))

        except ZeroDivisionError:
            return "You cannot divide by zero."

        except Exception:
            return "I could not understand that calculation."

    else:
        return "I don't know that yet. Try another question."


# ==================================================
# 8. MAIN FRANEJ INTERFACE
# ==================================================

def start_franej():

    print("=" * 50)
    print("             WELCOME TO FRANEJ")
    print("                  VERSION 3.2")
    print("=" * 50)

    print("Your personal educational AI assistant.")
    print("Type HELP to see available commands.")
    print("Type EXIT to close FRANEJ.")

    while True:

        message = input("\nYou: ").strip()

        command = message.lower()

        if command == "exit":
            print("FRANEJ: Goodbye! Thank you for using FRANEJ.")
            break

        elif command == "help":

            print("\nFRANEJ COMMANDS")
            print("1. CHAT - Basic conversation")
            print("2. TIME - Current time and date")
            print("3. CALCULATE - Simple mathematics")
            print("4. ALGEBRA - Solve linear equations")
            print("5. QUADRATIC - Solve quadratic equations")
            print("6. POLYNOMIAL - Evaluate polynomials")
            print("7. PHYSICS - Physics calculations")
            print("8. EXIT - Close the system")

        elif command == "time":
            time_system()

        elif command == "algebra":
            solve_linear()

        elif command == "quadratic":
            quadratic_solver()

        elif command == "polynomial":
            polynomial_engine()

        elif command == "physics":
            physics_engine()

        elif command.startswith("calculate "):

            print("FRANEJ:", franej_response(message))

        else:

            print("FRANEJ:", franej_response(message))


# ==================================================
# 9. START FRANEJ
# ==================================================

if __name__ == "__main__":
    start_franej()

# END OF FRANEJ VERSION 3.2
