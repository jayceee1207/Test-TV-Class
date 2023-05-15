#John Carlo Ablay
#Test TV Class
#May 13, 2023

import pyfiglet
import emoji
from pyfiglet import Figlet


from TV import TV

design = ("*********************************************************")
subject_name = ("Program: Class TV")
program_name = Figlet(font='banner3-D')
author_name = ("Programmed by: John Carlo R. Ablay")

design_center = design.center(120)
subject_name_center = subject_name.center(120)
author_name_center = author_name.center(120)

print("\u001b[35;1m", design_center)
print("\u001b[33;1m", subject_name_center)
print("\u001b[33;1m",author_name_center)
print("\u001b[35;1m",design_center)


tv_1 = TV()
tv_1.turn_on()
tv_1.set_channel(12)
tv_1.volume_up()
tv_1.volume_up()
tv_1.volume_up()


tv_2 = TV()
tv_2.turn_on()
tv_2.set_channel(31)
tv_2.volume_up()

print("\u001b[37;1m""Tv1-[Status]:") 
tv_1.display_result()

print("\u001b[37;1m""Tv2-[Status]:") 
tv_2.display_result()


