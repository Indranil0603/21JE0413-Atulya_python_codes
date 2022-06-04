def operation(num1, operator, num2):
    if operator == "+":
        return num1+num2
    if operator == "-":
        return num1 - num2
    if operator == "/":
        return num1 / num2
    else:
        return num1 * num2


a = int(input("Enter number 1: "))
op = str(input("Enter a operation: "))
b = int(input("Enter number 2: "))
c = operation(a, op, b)
print(c)