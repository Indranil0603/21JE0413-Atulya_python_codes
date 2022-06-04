def duplicate(a):
    frequency = {}
    for i in range(100):
        if a[i] in frequency:
            frequency[a[i]] += 1
        else:
            frequency[a[i]] = 1
        if frequency[a[i]] > 1:
            return a[i]
    return None


b = []
for i in range(100):
    d = str(input())
    b.append(d)

c = duplicate(b)
print("Deplicate is: ", c)
