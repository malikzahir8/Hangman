import random

ordlista = ["test", "mat", "dator", "vatten", "lektion", "ö"]

#list.append()
#list.pop()

ord = random.choice(ordlista)
gissnar = ""
antalgissnar = 0
felbok = []
antalgissnar2 = 10

while antalgissnar <= 10:
    fel = 0
    for x in ord:
        if x in gissnar:
            print(x, end="")
        else:
            print(" ___ ", end="")
            fel = fel + 1
    if fel == 0:
        print("Grattis Du vann!")
        break
    
    svar = str(input("\n \n Ange ett bokstav här:")).lower()
    gissnar = gissnar + svar

    if svar not in ord:
        antalgissnar2 = antalgissnar2 - 1
        print("FEL bokstav!")
        print(f"Du har {antalgissnar2} antalgissnar kvar")

        if antalgissnar2 <= 0:
            print("Du förlorade!!")
            break