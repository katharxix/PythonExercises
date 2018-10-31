print("convert strings")
word = input("Type a word: ")
output = ""
for i in word:
    if i.islower():
        output =output+i.upper()
    elif i.isupper():
        i.lower()
        output = output+i.lower()

print(output)


