def order(l1, ord1):  # the required function
    if ord1 == "asc":  # for sorting the list in ascending order
        for i in range(len(l1) - 1):
            for j in range(len(l1) - i - 1):
                if l1[j] > l1[j+1]:
                    l1[j], l1[j+1] = l1[j+1], l1[j]
        return l1
    elif ord1 == "desc": # for sorting the list in descending order
        for i in range(len(l1) - 1):
            for j in range(len(l1) - i - 1):
                if l1[j] < l1[j+1]:
                    l1[j], l1[j+1] = l1[j+1], l1[j]
        return l1
    else:
        return l1


lis =[]
n = int(input("Enter no of elements of  list: "))
for i in range(n):
    a = int(input())
    lis.append(a)
b = str(input("Enter the order (asc,desc,none): "))
c = order(lis, b)
print(c)



