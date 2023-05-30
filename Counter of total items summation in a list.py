my_list = [1,2,3,4,5,6,7,8,9,10]
# For printing out the initial count of the members in the list
for count in range(len(my_list)):
  count +=1
print(count)

# Now we will create a counter which will sum up the members in the list and give the total
counter = 0
for item in my_list:
  counter = counter + item
print(counter)