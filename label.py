# a simple code just for fun(:

import pyfiglet
from termcolor import colored

ascii_art = pyfiglet.figlet_format("Viter", font="basic")

colored_art = colored(ascii_art, color="red")


print(colored_art)

