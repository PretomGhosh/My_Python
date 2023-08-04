inputs = input("Enter a comma separated string of numbers : ").split(",")
print(inputs)
digits = []
for digit in inputs:
    digit = int(digit)
    digits.append(digit)
print(digits)
results = [item*item for item in digits if item%2 != 0]
print(results)