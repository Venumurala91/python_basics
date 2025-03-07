class parent:
    parentname = "srinivas"


class child(parent):

    def child_name(self, name):
        return name




a = child()
print(a.child_name("ravi"))
print(a.parentname)
# single inheritance
# above code is writted by me
# Below are the structured and corrected version both are true but below one adds some advantage
# ---------------------------------------# -
''''
what is self:
    Instance of the class
    Whenever we are creating an object in a class self refers to that object is called self
'''

class Mynumber:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)


obj1 = Mynumber(17)
obj1.print_value()

# ---------------------------------------------------------------------------------------------------------
class Parent:
    def __init__(self):
        self.parentname = "srinivas"  # Initialize parentname in the constructor


class Child(Parent):
    def child_name(self, name):
        return name  # Method to return the name passed

class child_son(Child):
    def child_son(self,son):
        return son

a=child_son()

print(a.child_name("ravi"))  # Output: ravi
print(a.parentname)  # Output: srinivas
print(a.child_son("kumar"))


# Above code belongs to multi level inheritance

# -------------------------------------------------------------------------------------------------------------------
# multiple inheritance : one class which is inherited from two or more class

class Parent1:
    def __init__(self):
        self.parent1_name = "somu"


class Parent2:
    def __init__(self):
        self.parent2_name = "ramu"


class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)  # Initialize Parent1
        Parent2.__init__(self)  # Initialize Parent2

    def call_child(self, name):
        return name


# Creating an instance of Child
c = Child()

# Accessing the attributes from both parent classes
print(c.parent1_name)  # Output: somu
print(c.parent2_name)  # Output: ramu

# Calling the child method
print(c.call_child("son"))  # Output: son


# ------------------------------------------------------------------------------------------------------------------------
# polymorprism
#
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

'''
In polymorpism we have two types 
1.Method overloading 
2.Method overriding 

Method overloading means : Two or more methods having same method name but different parameters is called method overloading 

ex :
'''



class calculator:
    def add(self, *args):
        return sum(args)

c=calculator()
print(c.add(2,3))
print(c.add(5,10))
print(c.add(10,20))


# class Calculator:
#     def add(self, *args):
#         return sum(args)
#
# # Creating an instance of Calculator
# calc = Calculator()
#
# # Calling add method with different numbers of arguments
# print(calc.add(5, 3))  # Output: 8
# print(calc.add(5, 3, 2))  # Output: 10
# print(calc.add(5))  # Output: 5
# print(calc.add(1, 2, 3, 4, 5))  # #

'''
Method overrriding
The
child
class method has the same name, same parameters, but a different behavior than the method in the parent class.
'''
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")  # Dog-specific sound

class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")  # Cat-specific sound

# Create objects of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the sound method on both objects
dog.sound()  # Output: Woof! Woof! (method overridden in Dog)
cat.sound()  # Output: Meow! Meow! (method overridden in Cat)
#
#
# polymorphish and its types is completed
# ----------# ------------------------------------------------------------------------------------------------------------
