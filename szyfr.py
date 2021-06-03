
def szyfr(tekst):
    new_text = ""
    for sign in tekst:
        if sign == "A" or "a":
            new_text += "C"
        elif sign == "B" or "b":
            new_text += "M"
        elif sign == "C" or "c":
            new_text += "R"
        elif sign == "D" or "d":
            new_text += "F"
        elif sign == "E" or "e":
            new_text += "Z"
        elif sign == "F" or "f":
            new_text += "S"
        elif sign == "G" or "g":
            new_text += "L"
        elif sign == "H" or "h":
            new_text += "N"
        elif sign == "I" or "i":
            new_text += "D"
        elif sign == "J" or "j":
            new_text += "G"
        elif sign == "K" or "k":
            new_text += "K"
        elif sign == "L" or "l":
            new_text += "O"
        elif sign == "M" or "m":
            new_text += "Q"
        elif sign == "N" or "n":
            new_text += "T"
        elif sign == "O" or "o":
            new_text += "P"
        elif sign == "P" or "p":
            new_text += "U"
        elif sign == "Q" or "q":
            new_text += "V"
        elif sign == "R" or "r":
            new_text += "W"
        elif sign == "S" or "s":
            new_text += "J"
        elif sign == "T" or "t":
            new_text += "H"
        elif sign == "U" or "u":
            new_text += "B"
        elif sign == "V" or "v":
            new_text += "E"
        elif sign == "W" or "w":
            new_text += "Y"
        elif sign == "X" or "x":
            new_text += "A"
        elif sign == "Y" or "y":
            new_text += "X"
        elif sign == "Z" or "z":
            new_text += 'I'
        else:
            new_text += sign

    return new_text
