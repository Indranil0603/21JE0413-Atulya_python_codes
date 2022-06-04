a = int(input("Enter lower limit: "))
b = int(input("Enter higher limit "))
print("Prime numbers in range ", a, " to ", b, ": ")
for i in range(a, b+1):
    for j in range(2,i//2):
        if i % j == 0:
            break
    else:
        print(i)