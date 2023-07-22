class two_methods:
    def __init__(self):
        self.name = None
        self.age = None

    def get_string(self):
        self.name = input("Please enter your name : ")
        self.age = input("Please enter your age : ")

    def print_string(self):
        print(f"This is {self.name} and this person's age is {self.age}")

Person = two_methods()
Person.get_string()
Person.print_string()