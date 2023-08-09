details = []  # Taken 3 empty lists
print("Enter your details here in Name,Age, Score format. Press Enter on an empty line to finish. ")  # Prompt for entering the details
while True:
    detail = input()
    if not detail:
        break
    parts = detail.split(',')
    if len(parts) == 3:
        details.append(tuple(parts))
    else:
        print("Invalid input. Please enter the details in the format: Name,Age,Score")
print(details)
def custom_sort_key(item):
    name, age, score = item
    return (name, int(age), int(score))  # Converted age and score to integers for numeric comparison

sorted_details = sorted(details, key=custom_sort_key)

print(sorted_details)


