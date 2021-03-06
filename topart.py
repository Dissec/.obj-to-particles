import os
from time import sleep
currentpath = os.path.dirname(os.path.realpath(__file__))
tag = 'assets'
color1 = 0
color2 = 0
color3 = 0
while True:
    name = str(input(f"File name: "))
    if name[-1:-5:-1] != 'jbo.':
        name = (name +".obj")
    color = str(input("Do you want to use colors? (y/n): ")).lower()
    if color == 'y':
        print("Using RGB color scheme")
        color1 = int(input("Red: (0-255): "))
        color2 = int(input("Green: (0-255): "))
        color3 = int(input("Blue: (0-255): "))
    w = open(f"{currentpath}\{tag}\mid.txt", "w")
    r = open(f"{currentpath}\{tag}\{name}", "r")
    def treat():
        if line[0] == 'v':
            if line[1] == ' ':
                w.write(line)
    with open(f'{currentpath}\{tag}\{name}') as read:
        for i in read:
            for line in read:
                treat()
    w.close()
    w = open(f"{currentpath}\out.mcfunction", "w")
    with open(f'{currentpath}\{tag}\mid.txt') as f:
        for line in f:
            cline = (line.replace("v", "^"))
            cline = cline.replace("\n", "")
            cline = cline[1:]
            cline = cline.replace(" ", " ^")
            cline = cline[1:]
            result = ("particle dust " + str(color1 / 255) + " " + str(color2 / 255) + " " + str(color3 / 255) + " 1 " + cline + " 0 0 0 0 1 force")
            w.write(result + "\n") 
    w.close()
    for i in range(0, 101, 5):
        print(f'{i}%')
        sleep(0.15)
    print("Conversion Finished")
    cont = str(input("Do you want to continue? y/n ")).lower()
    if cont == 'n':
        break
