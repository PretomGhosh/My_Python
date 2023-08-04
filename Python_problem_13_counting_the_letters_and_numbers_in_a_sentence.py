string = input("Enter a string : ")
letters = []
numbers = []
for char in string:
    if char.isalpha():
        letters.append(char)
    elif char.isdigit():
        numbers.append(char)
    else:
        continue
print(f'The number of letters in the string are {len(letters)} and number of digits are {len(numbers)}')