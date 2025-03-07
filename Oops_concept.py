# Oops in python
# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to organize code. Reusable , Easier to maintain


# A class is a blueprint or template for creating objects.
# It defines the properties (attributes) and behaviors (methods) that the objects of the class will have

# 2. Object
# An object is an instance of a class. It contains the data and methods defined in the class.\

# The core concepts of OOP in Python are:

# Class
# Object
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction


class Car:
    Company = "TATA"  # Class attribute

    def __init__(self, name, price):
        self.name = name  # Instance attribute
        self.price = price  # Instance attribute


# Creating an object of the Car class
car1 = Car("Tata Curve", "200000")

print(car1.name)
print(car1.Company)


# what is __init__ in above code

# __init__ is a method or constructor .
# It calls when an new object or instance is created  then automatically calls __init__ method .


# ---------------------------------------------><--------------------------------------------------------------------


# class variables and instance variables

# class variables:
#     These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods.


# Instance variables:
#     Variables that are unique to each instance (object) of a class. These are defined within the __init__ method or other instance methods.


# Example code :

class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age


# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)  # (Instance variable)
print(dog2.name)  # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)  # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)


# Output :

#             Output
#             Canine
#             Buddy
#             Charlie
#             Max
#             Feline
#             Feline


# Explanation:

# Class Variable (species): Shared by all instances of the class.
#   Changing Dog.species affects all objects, as it’s a property of the class itself.
# Instance Variables (name, age): Defined in the __init__ method.
#   Unique to each instance (e.g., dog1.name and dog2.name are different).
# Accessing Variables: Class variables can be accessed via the class name (Dog.species) or an object (dog1.species).
#   Instance variables are accessed via the object (dog1.name).


# Python Inheritance:
#     Inheritance allows a class (child) inherits properties or methods from another class (parent class)
#     Ex:
#         A child property which is inherited from their parents

# Types of inheritance :

#     Single Inheritance: A child class inherits from a single parent class.
#     Multiple Inheritance: A child class inherits from more than one parent class.
#     Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
#     Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
#     Hybrid Inheritance: A combination of two or more types of inheritance.


# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")


class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")


# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name} - Guides the way!")


# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")


class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")


# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()


# Explanation:

# Single Inheritance: Labrador inherits Dog’s attributes and methods.
# Multilevel Inheritance: GuideDog extends Labrador, inheriting both Dog and Labrador functionalities.
# Multiple Inheritance: GoldenRetriever inherits from both Dog and Friendly.

# -----------------------------------------------------------------------><-------------------------------------------------------------------------

#
# Python Polymorphism :

# Polymorphism allows methods to have the same name but behave differently based on the object’s context.
#  It can be achieved through method overriding or overloading.

# Parent Class
class Dog:
    def sound(self):
        print("dog sound")  # Default implementation


# Run-Time Polymorphism: Method Overriding
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")  # Overriding parent method


class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")  # Overriding parent method


# Compile-Time Polymorphism: Method Overloading Mimic
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c  # Supports multiple ways to call add()


# Run-Time Polymorphism
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound()  # Calls the appropriate method based on the object type

# Compile-Time Polymorphism (Mimicked using default arguments)
calc = Calculator()
print(calc.add(5, 10))  # Two arguments
print(calc.add(5, 10, 15))  # Three arguments


# -----------------------------------------------------------------------------------------><----------------------------------------


#  Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions.

# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

# Types of Encapsulation:
# Public Members: Accessible from anywhere.
# Protected Members: Accessible within the class and its subclasses.
# Private Members: Accessible only within the class..


class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class
# print(dog.__age)
# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())

# ----------------------------------------------------------------------------------------------------><-------------------------------------------------------------------




# super() funtion in python
#
# super method is used to call parent class to use thier keywords 0r attributes
# ->Also it is used to create additional fields in child classes
#
# ex:

class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add

# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails

Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)



