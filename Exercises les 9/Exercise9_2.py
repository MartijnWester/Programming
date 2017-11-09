import csv
import time

bestand = "inloggers.csv"

with open(bestand, "a") as file:
    writer = csv.writer(file, delimiter=";", lineterminator='\n')

    while True:
        naam = input("Wat is je achternaam: ")
        if naam == "einde":
            break
        voorl = input("Wat zijn je voorletters: ")
        gbdatum = input("Wat is je geboortedatum: ")
        email = input("Wat is je e-mailadres: ")

        date = time.strftime('%a %d %b %Y at %H:%M',time.localtime())
        writer.writerow((date,naam,voorl,gbdatum,email))