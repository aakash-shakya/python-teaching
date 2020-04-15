
class Person:
    # name = 'aakash'
    # name = 'rohan'
    # age = 18
    # address = 'Lubhu'
    def __init__(self,name=None,age=None,address=None,college=None):
        self.name = name
        self.age = age
        self.address = address
        self.college = college


    def ShowName(self):
        return(self.name)
    
    def ShowAge(self):
        print (self.age)
    
    def ShowAddress(self):
        return self.address
    
    def ShowCollege(self):
        return self.college

# # name = input('name:     ')
# # age = int(input('age:   '))
# # address = input('address:   ')

# # man = Person(name='aakash',address='lubhu',age=18,college="st.xavier's")
# # man_name = man.ShowName()
# # man_age = man.ShowAge()
# # man_address = man.ShowAddress()
# # man_college = man.ShowCollege()

# # print(man_name, man_age, man_address,man_college)


class Student(Person):
    def __init__(self,name,age,address,college):
        Person.__init__(self,name,age,address)
        self.college = college

    def study(self):
        super().ShowAge()
        print('I study computers')
        
    def changes(self):
        super().ShowCollege()
    
    def ShowCollege(self):
        print('this is a student college')

Lazah = Student(name="akash",age=18,address="lubhu",college="st.xaviers")
print(Lazah.ShowCollege())
name=Lazah.ShowName()
print(name)
age = Lazah.ShowAge()
print(age)
print(Lazah.ShowAddress())
Lazah.study()



# class Person:     
  
#         # __init__ is known as the constructor          
#         def __init__(self, name, idnumber):    
#                 self.name = name 
#                 self.idnumber = idnumber 
#         def display(self): 
#                 print(self.name) 
#                 print(self.idnumber) 
  
# # child class 
# class Employee( Person ):            
#         def __init__(self, name, idnumber, salary, post): 
#                 self.salary = salary 
#                 self.post = post 
  
#                 # invoking the __init__ of the parent class  
#                 Person.__init__(self, name, idnumber)  
  
                  
# # creation of an object variable or an instance 
# a = Person('Rahul', 886012)     
  
# # calling a function of the class Person using its instance 
# a.display()
