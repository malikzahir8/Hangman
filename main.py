import random, time


# bild
while True:
    print("Hänga Gubben")
    start = input("Om du vill starta spelet skriv S, om inte skriv end").lower()
    if start == "s":
        print("Nu kör vi!")
        pass
    
    elif start == "end":
        print("Varför inte!")
        break
    else:
        print("S för start \nEnd för avbryta")

