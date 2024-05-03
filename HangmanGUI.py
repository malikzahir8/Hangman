import PySimpleGUI as sg, ordfil, random, funktioner

ord = random.choice(ordfil.ordlista)

gissnar = ""
felbok = []
antalgissnar = 10

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

theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("BrownBlue")

while antalgissnar > 0:
    event, values = window.read()

    if len(gissnar) == len(ord) and gissnar in ord:
        sg.popup("Grattis! Du vann!")
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event == "End" or event == sg.WINDOW_CLOSED:
        sg.popup("Varför inte!")
        break

    if event == "Gissa":
        svar = values["-Gissning-"].lower()
        if len(svar) == 1:
            if svar in gissnar or svar in felbok:
                sg.popup("Du har redan gissat bokstaven!")
            else:
                gissnar += svar
                if svar not in ord:
                    felbok.append(svar)
                    antalgissnar -= 1
                    sg.popup(f"Fel bokstav! Du har {antalgissnar} antal gissnar kvar.")
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

    for x in ord:
        if x in gissnar:
            print(f" {x}  ", end="")
        else:
            print("___  ", end="")
    print()

    print(f"Bokstäverna som du gissade fel är: {felbok}")

if antalgissnar == 0:
    sg.popup("Du förlorade!")


window.close()