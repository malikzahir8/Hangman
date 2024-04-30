import PySimpleGUI as sg, ordfil

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = "Helvetica 14", button_element_size = (6,3))
    button_size = (6,3)
    layout = [[sg.Text("", font = "Helvetica 26", justification = "right", expand_x = True, pad = (10,20), right_click_menu = theme_menu, key = "-TEXT-")],      
        [sg.Button("Clear", expand_x = True), sg.Button("Enter", expand_x = True)],
        [sg.Button(1, size = button_size),sg.Button(2, size = button_size),sg.Button(3, size = button_size),sg.Button("-", size = button_size)],
        [sg.Button(0, expand_x = True),sg.Button(".", size = button_size),sg.Button("+", size = button_size)],
        ]  
    return sg.Window("Hänga Gubben", layout)

theme_menu = ["menu",["LightGrey1","DarkTeal1","DarkGray8", "DarkRed", "BluePurple", "BrightColors", "BrownBlue", "Dark",]]
window = create_window("BrownBlue") 

cn = []
op = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event in ["0","1","2","3","4","5","6","7","8","9","."]:
        cn.append(event)
        num_string = "".join(cn)
        window["-TEXT-"].update(num_string)
        
    if event in ["+","-","/","*"]:
        op.append("".join(cn))
        cn = []
        op.append(event)
        print(op)
        window["-TEXT-"].update("")
        
    if event == "Enter":
        op.append("".join(cn))
        result = eval(" ".join(op))
        window["-TEXT-"].update(result)
        op = []
    
    if event == "Clear":
        cn = []
        op = []
        window["-TEXT-"].update("")

window.close()