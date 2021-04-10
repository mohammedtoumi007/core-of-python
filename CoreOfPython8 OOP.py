# ******* objected oriented proramming *******
# A class is a blueprint, a model for its objects (type of object).
# A class defines a data type, its contains attributes and properties and methodes
# An instance is an objects of a class created at run-time
# Encapsulation :  Building (or wrapping) code and data together into a signale unit
# A class can inherit attributes and behavior (methods) from classes, called super-classes
# Polymorphism : lets you use the same word to mean different things in different contexts
# Data Hiding : prevent access to methods or variables outside the class

# ******* Adventage of objected oriented proramming *******
# OOPs makes development and maintenance easier where as in procedure oriented programming language it is not easy to manage if code grows as project size grows.
# OOPs provides data hiding and encapsulation whereas in procedure oriented programming language a global data can be accessed from anywhere.
# OOPs provides ability to simulate real-world event much more effectively like inheritance, polymorphism,... We can provide the solution of real word problem if we are using the objec oriented programming language.

# ******* Creating a class and an object *******
class Person:
    def say_hello(self):
        print("hello")
p = Person()
p.say_hello()

# ******* Constructor and Destructors*******
class Person:
    # constructor or initializer
    def __init__(self, name):
        self.name = name
    # method which returns a string
    def whoami(self):
        return "I am" +" "+self.name
    #destructors
    def __del__(self):
        print("I have been deleted")
p1 = Person("mohammed")
print(p1.whoami())
print(p1.name)
del p1

# ******* Operator Overloading*******

# + : __add__(self, other) / Addition
# * : __mul__(self, other) / Multiplication
# - : __sub__(self, other) / Subtraction
# % : __mod__(self, other) / Remainder
# / : __truediv__(self, other) / Division
# < : __lt__(self, other) / Less Than
# <= : __le__(self, other) / Less Than or equal to
# == : __eq__(self, other) / Equal To
# != : __ne__(self, other) / Not Equal To
# > : __gt__(self, other) / Greater than
# >= : __ge__(self, other) / Greater than or equal to
# [index] : __getitem__(self, index) / Index operator
# in : __contains__(self, value) / Check membership
# len : __len__(self) / The number of elements
# str : __str__(self) / The string representation

# ******* Operator Overloading Example*******
import math
class Circle:
    def __init__(self, radius): self.__radius = radius
    def setRadius(self, radius): self.__radius = radius
    def getRadius(self): return self.__radius
    def area(self): return math.pi * self.__radius ** 2
    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)
    def __gt__(self, another_circle):
        return self.__radius > another_circle.__radius
    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius
    def __str__(self):
        return "Cicle with radius" +" "+str(self.__radius)
c1 = Circle(4)
print(c1.getRadius())
c2 = Circle(5)
print(c2.getRadius())
c3 = c1 + c2
print(c3.getRadius())
print("c3 > c2 :", c3 > c2) # __gt__method
print("c3 > c2 :", c1 < c2) #__lt__method
print(c3) #__str__method

# ******* Inheritance*******
class MySuperClass1():
    def method_super1(self):
        print("method_super1 method called")
class MySuperClass2():
    def method_super2(self):
        print("method_super2 method called")
class ChildClass(MySuperClass1, MySuperClass2):
    def child_method(self):
        print("child method")
c = ChildClass()
c.method_super1()
c.method_super2()

# ******* Overriding methods*******
class A():
    def __init__(self):
        self.__x = 1
    def m1(self):
        print("m1 from A")
class B(A):
    def __int__(self):
        self.__y = 1
    def m1(self):
        print("m1 from B")
c = B()
c.m1()

# ******* Overriding methods*******
class Encapsulation(object):
    def __init__(self, a, b, c):
        self.public = a
        self.protected = b
        self.__private = c
x = Encapsulation(11, 13, 17)
print(x.public)
print(x.protected)
x._protected = 23
print(x._protected)
print(x.__private)

# Name : public = can be accessed from inside and outside
# _name : protected = like a public member, but they shouldn't be directly accessed from outside
# __name : private = can't be seen and accessed from outside

