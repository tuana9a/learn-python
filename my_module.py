import my_modules.test
my_modules.test.prin("hi hi")

# =======================================================
import my_modules.sound.effects.echo
my_modules.sound.effects.echo.echo_helloworld()

# =======================================================
from my_modules.sound.effects import echo
echo.echo_tuana9a()

# =======================================================
from my_modules.sound.effects.echo import *
echo_helloworld()

# =======================================================
# from sound.effects import *
# NOTE: this import cant do any thing with empty __init__.py

# =======================================================
from my_modules.sound.filters import *
# NOTE: this import all int __all__=['module1', 'module2']
karaoke.karaoke_mode("on")
# CAUTION: error because only karoke is loaded
# equalizer.increase_bass(10)

# =======================================================
# from sound.effects import echo
# echo.echo_reverse('co cc')

from my_modules.sound.filters import karaoke
karaoke.equalizer.decrease_bass(1)
karaoke.karaoke_with_bass()