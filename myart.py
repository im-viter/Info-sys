# a simple code just for fun(:

import pyfiglet
from termcolor import colored

ascii_art = pyfiglet.figlet_format(" Viter Society ", font="small")
# text = pyfiglet.figlet_format("Society", font="linux")
colored_art = colored(ascii_art, color="yellow")
# color = colored(text, color="magenta")

print(colored_art)
# print(color)
