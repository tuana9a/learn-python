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
# p1

# kế thừa class Person
class Student(Person):
  def __init__(mysillyobject, name, age):
    super().__init__(name, age)
  pass

s = Student("tuana9a", 12)
s.myfunc()

class Duck:
    sound='quackk'
    walking='walk like a duck'
    def hello(self):
        print(self.sound)
d = Duck()
d.hello()

class Test1():
  def __init__(self, name):
    super().__init__()
    self.test1 = f'hi im {name}'
    
  @property
  def name(self):
    return f'my test1 is {self.test1}'
    
  @classmethod
  def name1(cls):
    return f'"co con cac day la class "' + str(cls)


# print(Test1("tuan").name)
print(Test1("tuan").name1)
print(Test1("tuan").name1())
print(Test1.name1)
print(Test1.name1())