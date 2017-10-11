def kwadraten_som(getallenlijst):
    kwadraat = []
    for getal in getallenlijst:
        if getal > 0:
            kwadraat.append(getal**2)
        else:
            continue
    print(sum(kwadraat))
kwadraten_som([1, 2, 3, 4, 8, -112])
