
# Conventional approach
numbers = []
for i in range(2000, 3201):
    if (i % 7 == 0 and i % 5 != 0):
        numbers.append(i)
    else:
        continue
numbers = [str(num) for num in numbers]
print(','.join(numbers))

# Using generators and making an one line code
print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep= ',' )
