getallenlijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def som(lijst):
    getal=0
    for elkewaarde in lijst:
        getal+=elkewaarde

    return getal
x=som(getallenlijst)
print (x)