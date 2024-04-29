import PySimpleGUI as sg, ordfil, random

ord = random.choice(ordfil.ordlista)

layout = [  [sg.Text("| Gissa bokstaven ner: |")],
            [sg.InputText()],
            [sg.Button("OK")]]

window = sg.Window('Hangman', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    ord = random.choice(ordfil.ordlista)
    gissnar = ""
    antalgissnar = 0
    antalgissnar2 = 10
    while antalgissnar <= 10:
        svar = values[0]
        fel = 0
        for x in ord:
            if x in gissnar:
                print(x, end="")
            else:
                print("   ___ ", end="")
                fel = fel + 1
        if fel == 0:
            print("\n   Grattis Du vann!")
            break
        gissnar = gissnar + svar 
        if svar not in ord:
            antalgissnar2 = antalgissnar2 - 1
            print("  FEL bokstav!")
            print(f"  Du har {antalgissnar2} antalgissnar kvar")
            if antalgissnar2 <= 0:
                print("  Du förlorade!!")
                break

window.close()
