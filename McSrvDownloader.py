import downloaders as dl
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
stype = input("\n? | Select Server Type: ")

###

if not stype in dl.types:
    print("! | Invalid type")

elif stype == "vanilla":
    dl.vanilla()

elif stype == "paper":
    dl.papermc()
