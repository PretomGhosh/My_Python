numbers = [x for x in range(1000, 3001)]
print(numbers)
results = [num for num in numbers if all(int(digit) % 2 == 0 for digit in str(num))]
print(results)
