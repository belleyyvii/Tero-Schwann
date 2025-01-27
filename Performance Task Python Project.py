# Setup string variables
operator = input("Enter an operator (+ - * /): ")
number1 = float(input("Enter the 1st number: "))
number2 = float(input("Enter the 2nd number: "))

if operator == "+":    # This operator adds numbers
    result = number1 + number2
    print(round(result, 3))
elif operator == "-":  # This operator subtracts numbers
    result = number1 - number2
    print(round(result, 3))
elif operator == "*":  # This operator multiplies numbers
    result = number1 * number2
    print(round(result, 3))
elif operator == "/":  # This operator divides numbers
    result = number1 / number2 
    print(round(result, 3))
else:                  # It results to this syntaxerror when certain invalid numbers or operators are given by users
    print(f"{operator} is not a valid operator")
    
