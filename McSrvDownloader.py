import downloaders as dl
from downloaders.color import *
logo="""
███╗   ███╗███████╗██████╗ 
████╗ ████║██╔════╝██╔══██╗
██╔████╔██║███████╗██║  ██║
██║╚██╔╝██║╚════██║██║  ██║
██║ ╚═╝ ██║███████║██████╔╝
╚═╝     ╚═╝╚══════╝╚═════╝ 
"""
print(logo)

print("Available Types: "+", ".join(dl.types))
stype = input(c.GREEN+"? | Select Server Type: "+c.END)

###

if not stype in dl.types:
    print(c.RED+"! | Invalid type"+c.END)

elif stype == "vanilla":
    dl.vanilla()

elif stype == "paper":
    dl.papermc()

elif stype == "spigot":
    dl.spigotmc()