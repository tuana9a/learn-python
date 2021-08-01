class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " and I'm " + str(self.age) + " years old")

p1 = Person("John", 36)
p1.myfunc()

"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

del p1.age
del p1
p1

# kế thừa class Person
class Student(Person):
  pass

class Duck:
    sound='quackk'
    walking='walk like a duck'
    def hello(self):
        print(self.sound)
d = Duck()
d.hello()
