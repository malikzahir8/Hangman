import PySimpleGUI as sg, ordfil, random, funktioner

# random ord
ord = random.choice(ordfil.ordlista)

# variabel
gissnar = ""
felbok = []
antalgissnar = 10

# layout som vissas i fönstret
def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = "Helvetica 14", button_element_size = (1,3))
    layout = [[sg.Text("", font = "Helvetica 26", justification = "right", expand_x = True, pad = (10,20), right_click_menu = theme_menu, key = "-TEXT-")],
              [sg.Text("", size=(15, 10), key="-gubben-")],
              [sg.Text("Gissa ordet ner:")],
              [sg.Text(" ".join([x if x in gissnar else "___  " for x in ord]))],
              [sg.Input(key="-Gissning-", size=(32,3))],
              [sg.Button("Gissa", size=(15, 3)), sg.Button("End", size=(15, 3))]
              ]
    return sg.Window("Hänga Gubben", layout, element_justification="c")

# theme
theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("BrownBlue")

# while loop för hela programmet
while antalgissnar > 0:
    event, values = window.read()

    # Om man gissat rätt
    if len(gissnar) == len(ord) and gissnar in ord:
        sg.popup("Grattis! Du vann!")
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event == "End" or event == sg.WINDOW_CLOSED:
        sg.popup("Varför inte!")
        break
    # om man trycker på giss då händer det här
    if event == "Gissa":
        svar = values["-Gissning-"].lower()
        if len(svar) == 1:
            # om den nya gissning är med i felbokstäver eller ordet så har man gissat den innan
            if svar in gissnar or svar in felbok:
                sg.popup("Du har redan gissat bokstaven!")
            else:
                gissnar += svar
                # om gissningen är inte med i ordet
                if svar not in ord:
                    felbok.append(svar)
                    antalgissnar -= 1
                    # visar antal gissnar som är kvar
                    sg.popup(f"Fel bokstav! Du har {antalgissnar} antal gissnar kvar.")
                    # visar olika steg av gubben beronde på antal gissnar
                    if antalgissnar == 9:
                        funktioner.gubben1()
                    elif antalgissnar == 8:
                        funktioner.gubben2()
                    elif antalgissnar == 7:
                        funktioner.gubben3()
                    elif antalgissnar == 6:
                        funktioner.gubben4()
                    elif antalgissnar == 5:
                        funktioner.gubben5()
                    elif antalgissnar == 4:
                        funktioner.gubben6()
                    elif antalgissnar == 3:
                        funktioner.gubben7()
                    elif antalgissnar == 2:
                        funktioner.gubben8()
                    elif antalgissnar == 1:
                        funktioner.gubben9()
                    elif antalgissnar == 0:
                        funktioner.gubben10()
                        break
                    else:
                        break
        else:
            sg.popup("Gissa bara en bokstav!")
    window["-Gissning-"].update("")

    # understreck system
    for x in ord:
        if x in gissnar:
            print(f" {x}  ", end="")
        else:
            print("___  ", end="")
    print()
    # felbokstäver vissa har i en lista
    print(f"Bokstäverna som du gissade fel är: {felbok}")

# om antalgissnar är 0 då förlorar man
if antalgissnar == 0:
    sg.popup("Du förlorade!")

# för att stänga ner programmet
window.close()