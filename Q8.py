a = str(input("Enter a string: "))
b = 0
for i in range(len(a)):
    if a[i].isdigit():
        b += int(a[i])
print(b)