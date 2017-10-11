lijst = ['a', 'b', 'c']
print(lijst)


def wijzig(letterlijst):
    """de functie leegt de lijst en voegt de letters ['d', 'e', 'f'] toe"""
    lijst.remove('a')
    lijst.remove('b')
    lijst.remove('c')
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')


wijzig(lijst)
print(lijst)