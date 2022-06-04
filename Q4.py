def double1(word):
    word1 = ""
    for i in range(len(word)):
        word1 += 2*word[i]
    return word1


a = str(input("Enter a string: "))
b = double1(a)
print(b)