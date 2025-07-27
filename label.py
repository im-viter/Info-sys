# a simple code just for fun(:

import pyfiglet
from termcolor import colored

ascii_art = pyfiglet.figlet_format("Viter", font="basic")
# text = pyfiglet.figlet_format("Society", font="linux")
colored_art = colored(ascii_art, color="red")
# color = colored(text, color="magenta")

print(colored_art)
# print(color)
