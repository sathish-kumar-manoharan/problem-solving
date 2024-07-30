class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ''+ self.name + " is " + self.age + "years old"

class Student(Person):
    def __init__(self, id, name, age):
        self.id = id
        super().__init__(name, age)
    
    def __str__(self):
        return 'Id is ' + str(self.id) + " " + self.name + " is " + str(self.age) + "years old"

student = Student(1001, "sathish", 37)

list = []
list.append(Student(1001, "sathish", 37))
list.append(Student(1002, "Kumar", 32))
list.append(Student(1003, "Elves", 33))
list.append(Student(1004, "wolves", 35))

print(list)

[print("The name is ", str(x.name), " ", str(x.age)) for x in list]

print(list.sort(key = lambda x: x.age))

[print("The name is "+ x.name + " " + str(x.age)) for x in list]


print(list.sort(key = lambda x: x.age, reverse=True))

[print("The name is "+ x.name + " " + str(x.age)) for x in list]

print(list.sort(key = lambda x: x.age))

[print("The name is "+ x.name + " " + str(x.age)) for x in list]