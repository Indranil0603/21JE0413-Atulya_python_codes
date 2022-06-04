a = []
b = int(input("Enter the number of elements in the array: "))
for i in range(b):
    c= int(input())
    a.append(c)
frequency = {}
for i in range(b):
    if a[i] in frequency:
        frequency[a[i]] += 1
    else:
        frequency[a[i]] = 1
key = list(frequency.keys())
max = key[0]
for i in key:
    if frequency[i] > frequency[max]:
        max = i
print("The number ",max," has the highest frequency of", frequency[max])