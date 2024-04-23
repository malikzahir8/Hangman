import random, ordfil, gubben


#list.append()
#list.pop()

ord = random.choice(ordfil.ordlista)
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
        print("\nGrattis Du vann!")
        break
    
    svar = str(input("\n \nAnge ett bokstav här:")).lower()
    gissnar = gissnar + svar

    if svar not in ord:
        antalgissnar2 = antalgissnar2 - 1
        print("FEL bokstav!")
        print(f"Du har {antalgissnar2} antalgissnar kvar")
        
        if antalgissnar2 == 9:
            gubben.gubben1()
        elif antalgissnar2 == 8:
            gubben.gubben2()
        elif antalgissnar2 == 7:
            gubben.gubben3()
        elif antalgissnar2 == 6:
            gubben.gubben4()
        elif antalgissnar2 == 5:
            gubben.gubben5()
        elif antalgissnar2 == 4:
            gubben.gubben6()
        elif antalgissnar2 == 3:
            gubben.gubben7()
        elif antalgissnar2 == 2:
            gubben.gubben8()
        elif antalgissnar2 == 1:
            gubben.gubben9()
        elif antalgissnar2 == 0:
            gubben.gubben10()
        else:
            pass

        if antalgissnar2 <= 0:
            print("Du förlorade!!")
            break