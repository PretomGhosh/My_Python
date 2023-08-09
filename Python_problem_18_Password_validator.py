password = input("Password : ").split(",")  # This is for accepting a string of passwords from user input, normally only one password will be typed in real scenario
print(password)
symbols = ['$','#','@']
for item in password:
    val = True
    if len(item) < 6:
        print("Password must contain at least 6 characters")
        val = False
    if len(item) > 12:
        print("Password must not be more than 12 characters long")
        val = False
    if not any(char.isdigit() for char in item):
        print("Password must contain at least a digit from [0-9]")
        val = False
    if not any(char.isupper() for char in item):
        print("Password must contain at least one uppercase letter from [A-Z]")
        val = False
    if not any(char.islower() for char in item):
        print("Password must contain at least one lowercase letter from [a-z]")
        val = False
    if not any(char in symbols for char in item):
        print("Password must contain at least one symbol from [$,#,@]")
        val = False
    if ' ' in item:
        print("Password must not contain any blank space")
        val = False
    if val:
        print(f'Password is valid: {item}' )
