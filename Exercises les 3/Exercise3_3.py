age = int(input('Geef je leeftijd: '))
paspoort = str(input('Ben je in bezit van een Nederlands paspoort?: '))
if age >= 18 and paspoort == 'ja' or paspoort == 'JA':
    print('Gefeliciteerd!, je mag stemmen')
else:
    print('Helaas, je mag nog niet stemmen')