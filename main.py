import random, time, gubben, ordfil



while True:
    time.sleep(0.8)
    gubben.spelnamn()
    time.sleep(0.8)
    start = str(input("  Om du vill starta spelet skriv Start\n  Om inte skriv End: ")).lower()
    time.sleep(0.8)
    if start == "start" or start == "s":
        hurspelar = input("  Om du vill se hur spelet fungerar tryck på |?| ")
        if hurspelar == "?":
            print(f"  Hänga Gubben är ett gissningsspel där det slumpas fram ett ord och sedan gissar spelaren vilka bokstäver som finns i ordet \n \n")
        
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
            print(f"\n \n  Bokstäverna som du gissade fel är: {felbok}")
            time.sleep(0.8)
            svar = str(input("\n  Ange ett bokstav här:")).lower()
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
        print("  Start för att starta \nEnd för avbryta")
        time.sleep(0.8)

