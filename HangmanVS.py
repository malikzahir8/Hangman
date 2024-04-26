import random, time, funktioner, ordfil

# while loop för hela spelet
while True:
    time.sleep(0.8)
    funktioner.spelnamn()
    time.sleep(0.8)
    start = str(input("  Skriv\n  |Start för starta|\n  |End för avbryta| ")).lower()
    time.sleep(0.8)
    if start == "start" or start == "s":
        hurspelar = input("  Om du vill se hur spelet fungerar tryck på |?| ")
        if hurspelar == "?":
            funktioner.beskrivning()

        print(f"  Nu kör vi! \n \n")
        time.sleep(0.8)

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
                    print("   ___ ", end="")
                    fel = fel + 1
            if fel == 0:
                print("\n   Grattis Du vann!")
                time.sleep(0.8)
                break
            print(f"\n \n  |Bokstäverna som du gissade fel är: {felbok}")
            time.sleep(0.8)
            svar = str(input("\n  |Gissa ett bokstav här:")).lower()
            time.sleep(0.8)
            gissnar = gissnar + svar

            if svar not in ord:
                antalgissnar2 = antalgissnar2 - 1
                print("  FEL bokstav!")
                felbok.append(svar)
                time.sleep(0.8)
                print(f"  Du har {antalgissnar2} antalgissnar kvar")
                time.sleep(0.8)

                if antalgissnar2 == 9:
                    funktioner.gubben1()
                elif antalgissnar2 == 8:
                    funktioner.gubben2()
                elif antalgissnar2 == 7:
                    funktioner.gubben3()
                elif antalgissnar2 == 6:
                    funktioner.gubben4()
                elif antalgissnar2 == 5:
                    funktioner.gubben5()
                elif antalgissnar2 == 4:
                    funktioner.gubben6()
                elif antalgissnar2 == 3:
                    funktioner.gubben7()
                elif antalgissnar2 == 2:
                    funktioner.gubben8()
                elif antalgissnar2 == 1:
                    funktioner.gubben9()
                elif antalgissnar2 == 0:
                    funktioner.gubben10()
                else:
                    break

                if antalgissnar2 <= 0:
                    print("  Du förlorade!!")
                    time.sleep(0.8)
                    break
    
    elif start == "end":
        print("  Varför inte!")
        time.sleep(0.8)
        break
    else:
        print("  |Start för att starta| \n|End för avbryta|")
        time.sleep(0.8)

