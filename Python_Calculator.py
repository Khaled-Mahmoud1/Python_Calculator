# Simple Calculator Program 
# ---------------------------
# Features:
# - Handles invalid numeric input using try/except (ValueError).
# - Validates operators to accept only (+, -, *, /, %).
# - Prevents division by zero (ZeroDivisionError).
# - Uses Python's 'match-case' structure for cleaner operation handling.
# - Allows the user to repeat operations until they choose to exit.

status = True
while status:
    while True:
        try:
            num1=float(input("enter the  first num : "))
            break
        except ValueError:
            print("Invalid input , please enter a numeric value :")
    while True:
        try:        
            oper=input("enter an operator (+,-,*,/,%) : ")
            if oper in ("+","-","/","*","%"):
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid operation, please enter (+,-,/,*,%)")
    while True:
        try:
            num2=float(input("enter the second num : "))
            if num2 == 0 and oper == "/":
                raise ZeroDivisionError
            break
        except ValueError:
            print("Invalid input , please enter a numeric value :")
        except ZeroDivisionError:
            print("Invalid input , please enter another numeric value :")
    # if oper == "+":
    #     result = num1 + num2
    # elif oper == "-":
    #     result = num1 - num2
    # elif oper == "*":
    #     result = num1 * num2
    # elif oper == "/":
    #         result = num1 / num2
    # elif oper == "%":
    #     result = num1 % num2
    # else:
    #     result = None
    match oper:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            result = num1 / num2
        case "%":
            result = num1 % num2
        case _:
            result = None
    if result != None:
        print(f"{num1} {oper} {num2} = {result}")
    else:
        print("Unexpected Error")
    repeat = input("Do you want to perform another operation? (y/n) : ")
    if repeat == "n":
        status = False
print("Program Exited")
