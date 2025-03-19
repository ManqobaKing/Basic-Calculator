#Basic calculator program

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operation (+,-,/,*): ")

if operator == "+":
    sum = num1 +num2
    print(num1, " + ", num2, " = " ,sum)
elif operator == "-":
    diff = num1-num2
    print(num1, " - ", num2, " = " ,diff)
elif operator == "/":
    quotient = num1 / num2
    print(num1, " / ", num2, " = ", quotient)
elif operator == "*":
    product = num1 * num2
    print(num1, " * ", num2, " = ", product)
else:
    print("Invalid operator")
