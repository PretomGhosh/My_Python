#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Tom', 2)
cat2 = Cat('Han', 3)
cat3 = Cat('Meu', 4)


# 2 Create a function that finds the oldest cat
def Oldest_cat():
  oldest = None
  max_age = -1
  cats = [cat1, cat2, cat3]
  for cat in cats:
    if cat.age > max_age:
      max_age = cat.age
      oldest = cat
  return cat.name


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

oldest_cat = Oldest_cat()
print("The oldest cat is : ", oldest_cat)