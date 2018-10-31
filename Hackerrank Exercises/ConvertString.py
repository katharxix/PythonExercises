print("convert strings")
s = input("Type a word: ")

for i in s:
    if i.islower():
        print(i.upper())
    elif i.isupper():
        print(i.lower())

