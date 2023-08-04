binary_input = input("Enter 4 digit binary numbers separated by commas : ").split(",")
binary_numbers = [int(binary, 2) for binary in binary_input]
final = []
for item in binary_numbers:
    if item%5 == 0:
        item = bin(item)
        final.append(item)
    else:
        continue
final_result = [i[2:] for i in final]
print(",".join(final_result))