from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
all_fonts = figlet.getFonts()
argv_len = len(sys.argv)

if argv_len != 3:
    if argv_len == 1:
        font = all_fonts[random.randint(0 , len(all_fonts))]
    else:
        sys.exit("Invalid usage")
else:
    command, font = sys.argv[1], sys.argv[2]
    if command not in ["-f", "--font"] or font not in all_fonts:
        sys.exit("Invalid usage")


#print(font)
word = input("Input: ")
figlet.setFont(font=font)
print(figlet.renderText(word))



