# Conventional approach
input_string = input("Please enter comma separated numbers here : ")
li = list(input_string.split(","))
print(li)
tup = tuple(input_string.split(","))
print(tup)

# One line approaches

print(list(input("Please enter comma separated numbers here : ").split(",")))
print(tuple(input("Please enter comma separated numbers here : ").split(",")))