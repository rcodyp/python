class bazon:
    x=5

p1 = bazon()
print(p1.x)


class person:
    def __init__(self,name,age):
        self.name =name
        self.age = age

name=input('enter your name: ')
age = input('enter your age: ')
p1 = person('name',13)
print(p1.name)
print(p1.age)