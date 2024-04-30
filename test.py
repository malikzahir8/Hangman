import PySimpleGUI as sg, ordfil, random

ord = random.choice(ordfil.ordlista)
gissnar = ""
antalgissnar = 0
antalgissnar2 = 10
felbok = []

layout = [
    [sg.Text(key="understreck")],
    [sg.Text("| Gissa bokstaven ner: |")],
    [sg.Input(key="input")],
    [sg.Button("Gissa")],
    [sg.Text(key="meddelande")]
]

window = sg.Window('Hangman', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    while antalgissnar <= 10:
        bokstav = values["input"]
        fel = 0
        for x in ord:
            if x in gissnar:
                window["understreck"].update(x, end="")
            else:
                window["understreck"].update(" ___ ", end="")
                fel = fel + 1
        
        if fel == 0:
            window["meddelande"].update("Grattis du vann!")
            break
        gissnar = gissnar + bokstav 
        
        if bokstav not in ord:
            antalgissnar2 = antalgissnar2 - 1
            window["meddelande"].update("FEL Bokstav!!")
            window["meddelande"].update(f"Du har {antalgissnar2} antalgissnar kvar")

            if antalgissnar2 <= 0:
                window["meddelande"].update("Du förlorade!")
                break 

window.close()