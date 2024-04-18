import random

ordlista = ["test", "mat", "food", "vatten"]
n = random.randint(1,3)
print("___  ___  ___")



#list.append()
#list.pop()

def ord():
    ordet = ordlista[n]
    antalbokstav = len(ordet)
    print(antalbokstav)

ord()