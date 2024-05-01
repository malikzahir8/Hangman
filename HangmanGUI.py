import PySimpleGUI as sg, ordfil, random

ord = random.choice(ordfil.ordlista)

gissnar = ""
felbok = []
antalgissnar = 10

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = "Helvetica 14", button_element_size = (6,3))
    layout = [
    [sg.Text("Gissa ordet ner:")],
    [sg.Text(" ".join([x if x in gissnar else "___  " for x in ord]))],
    [sg.Input(key="-Gissning-")],
    [sg.Button("Gissa", size=(18, 4)), sg.Button("End", size=(18, 4))]
    ]
    return sg.Window("Hänga Gubben", layout)

theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("BrownBlue")

while antalgissnar > 0:
    event, values = window.read()
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    if event == "End" or event == sg.WINDOW_CLOSED:
        break
    if event == "Gissa":
        guess = values["-Gissning-"].lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in gissnar or guess in felbok:
                sg.popup("Du har redan gissat bokstaven!")
            else:
                gissnar += guess
                if guess not in ord:
                    felbok.append(guess)
                    antalgissnar -= 1
                    sg.popup(f"Fel bokstav! Du har {antalgissnar} antal gissnar kvar.")
        else:
            sg.popup("Gissa bara en bokstav!")
    window["-Gissning-"].update("")

    for x in ord:
        if x in gissnar:
            print(x, end="")
        else:
            print("___  ", end="")
    print()

    print(f"Bokstäverna som du gissade fel är: {felbok}")

if antalgissnar == 0:
    sg.popup("Du förlorade!")
else:
    sg.popup("Grattis! Du vann!")

window.close()