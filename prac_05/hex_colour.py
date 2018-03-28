COLOUR_HEX = {"blue": "#0000ff", "violet": "#8a2be2", "maroon": "#b03060", "magenta": "#ff00ff",
              "limegreen": "#32cd32", "navyblue": "#000080", "orange": "#ffa500", "orchid": "#da70d6",
              "pink": "#ffc0cb", "purple": "#a020f0",}


def main():
    colour = input("Enter a colour name: ").lower()
    if colour in COLOUR_HEX:
        print(colour, "is", COLOUR_HEX[colour])
    else:
        print("Invalid colour name")


main()
