age = int(input('Geef je leeftijd: '))
paspoort = str(input('Ben je in bezit van een Nederlands paspoort?: '))
if age >= 18 and paspoort == 'ja':
    print('Gefeliciteerd!, je mag stemmen')
else:
    print("helaas, je mag niet stemmen")