a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

a = b ^ a
b = b ^ a
a = b ^ a
print(a, b)