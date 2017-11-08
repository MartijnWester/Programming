file = open('Kaartnummer.txt')
lst = []
grootste = file.readlines()

for i in grootste:
    temp = i.split(sep=',')
    lst.append(eval(temp[0]))

waarde = max(lst)

y=0

for i in grootste:
    y = y+1
    if str(waarde) in i:
        print('Deze file telt ' + str(len(grootste)) + ' regels')
        print('Het grootste kaartnummer is: ' + str(waarde) + ' en dat staat op regel ' + str(y))

