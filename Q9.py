l1 = str(input("Enter a string: "))
l1 = list(l1)
l2 = ""
for i in range(len(l1) - 1):
    for j in range(len(l1) - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]
for i in range(len(l1)):
    l2 += l1[i]
print(l2)