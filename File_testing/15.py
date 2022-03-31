# myFile = open('File1.txt', 'rt', encoding='utf8')
# print(myFile.readline())
# myFile = open('File1.txt', 'rt', encoding='utf8')
# print(myFile.readlines())
# myFile = open('File1.txt', 'rt', encoding='utf8')
# for line in myFile:
#     print(line)
#
# myFile2 = open('File2.txt', 'w', encoding='utf8')
# myFile2.write('ttt')
# print('zzz', file=myFile2)
alpha = 'йцукенгшщзхъфывапролджэячсмитьбю'
alphaUp = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summury = ''

def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char
with open('File1.txt', 'rt', encoding='utf8') as myFile:
    for line in myFile:
        for char in line:
            summury += changeChar(char)

with open('output1.txt', 'w', encoding='utf8') as myFile:
    myFile.write(summury)