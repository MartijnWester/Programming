import func

weekend = input('is het weekend (ja/nee): ')
if weekend[0] in 'YJjy':
    weekend = 1
else: weekend = 0

leeftijd = eval(input('wat is uw leeftijd: '))
aantalKM = eval(input('Aantal KM: '))

print('De kosten voor de ticket bedraagt €' + str("%.2f" % func.ritprijs(leeftijd,weekend,aantalKM)))