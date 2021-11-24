x = 10
try:
    print(x)
except:
    print("An exception occurred")

del x
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

import platform

print("this is python version: {}".format(platform.python_version()))


print(__name__)


def test1():
    x = 1000000


test1()

# print(x) # Error x is not defined
if True:
    x = 11
print(x)

x = (1,2,3,4)
print(type(x))
x = [1,2,3,4]
print(type(x))
x = {1,3,4}
print(type(x))
x = range(1,10)
print(type(x))
x = range (1, 10, 3)
for l in x: print(l)
print(type(type("tuan")))
print(isinstance("tuan", str))
# print("tuan" is 'tuan')
# print("tuan" == 'tuan')


# =======================================================
# import sound.effects.echo
# sound.effects.echo.echo_helloworld()

# =======================================================
# from sound.effects import echo
# echo.echo_tuana9a()

# =======================================================
# from sound.effects.echo import *
# echo_helloworld()

# =======================================================
# from sound.effects import *
# NOTE: this import cant do any thing with empty __init__.py

# =======================================================
# from sound.filters import *
# NOTE: this import all int __all__=['module1', 'module2']
# karaoke.karaoke_mode("on")
# equalizer.increase_bass(10) # CAUTION: error because only karoke is loaded

# =======================================================
# from sound.effects import echo
# echo.echo_reverse('co cc')

from sound.filters import karaoke
karaoke.equalizer.decrease_bass(1)
karaoke.karaoke_with_bass()

from tuana9a import example
print(example.add_one(10))
