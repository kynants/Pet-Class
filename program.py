class Pet:
    # def __init__(self, name, type, age):
    #     self.name = name
    #     self.type = type
    #     self.age = age

    def set_name(name):
        n = name

    def set_type(type):
        t = type

    def set_age(age):
        a = age

    def get_name(name):
        print('Pet age: ', name)

    def get_type(type):
        print('Pet type: ', type)

    def get_age(age):
        print('Pet age: ', age)

p1 = Pet()
p1.name = input("Enter the pet's name: ")
p1.type = input("Enter the pet type: ")
p1.age = input("Enter the pet's age: ")

print("The pet is a", p1.type, "whose name is"
      , p1.name, "and is", p1.age, "years old.")