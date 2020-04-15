
# 4 pillars of oop

#  --> encapsulation

#  --> inheritance 
#  --> abstraction
#  --> polymorphism


class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = int(input('age: '))
        self.address = address

    def Show(self, x):
        self.y = x
        print(self.name, self.age, self.address, x)



class student(Person):
    def __init__(self,college,name,age,address):
        Person.__init__(self,name,age,address)
        self.college = college

    def ShowCollege(self):
        print(self.college,self.name,self.address)
    
    def Show(self):
        print(self.name, self.age)
    
