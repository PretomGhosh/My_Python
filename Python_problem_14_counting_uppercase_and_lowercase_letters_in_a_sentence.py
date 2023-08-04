sentence = input("Enter a sentence : ")
upper = []
lower = []
for char in sentence:
    if char.isupper():
        upper.append(char)
    elif char.islower():
        lower.append(char)
    else:
        continue
print(f'Total uppercase letters in the sentence are {len(upper)} and total lowercase letters are {len(lower)}')