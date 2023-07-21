# Using conventional approach
def factorial(number):
    if number < 0:
        print("Sorry, the number must be non negative, try again")
    elif number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return(number * factorial(number - 1))
    
number = input("Please input an integer number : ")
number = int(number)
print(factorial(number))

# Using lambda function and making it one line

def factorial_of_number(number):
    return 1 if number <=1 else number*factorial_of_number(number - 1)
print(factorial_of_number(number))