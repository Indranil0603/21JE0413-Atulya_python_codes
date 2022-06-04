def hiddenstring(num):
    num1 = ""
    for i in range(-4, 0, 1):
        num1 += num[i]
    return num1


b = str(input("Enter a ph no: "))
c = hiddenstring(b)
print(c)