import modules.test
modules.test.prin("hi hi")

# =======================================================
import modules.sound.effects.echo
modules.sound.effects.echo.echo_helloworld()

# =======================================================
from modules.sound.effects import echo
echo.echo_tuana9a()

# =======================================================
from modules.sound.effects.echo import *
echo_helloworld()

# =======================================================
# from sound.effects import *
# NOTE: this import cant do any thing with empty __init__.py

# =======================================================
from modules.sound.filters import *
# NOTE: this import all int __all__=['module1', 'module2']
karaoke.karaoke_mode("on")
# CAUTION: error because only karoke is loaded
# equalizer.increase_bass(10)

# =======================================================
# from sound.effects import echo
# echo.echo_reverse('co cc')

from modules.sound.filters import karaoke
karaoke.equalizer.decrease_bass(1)
karaoke.karaoke_with_bass()