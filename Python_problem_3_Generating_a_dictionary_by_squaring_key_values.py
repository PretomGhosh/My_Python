# Traditional approach
number = input("Please enter an integer number : ")
number = int(number)
result = {}
for i in range(1, number + 1):
    key = i
    value = i*i
    result[key] = value
print(result)

# Using dictionary comprehension method and reducing lines of codes

result_new = {i : i*i for i in range(1, number + 1)}
print(result_new)