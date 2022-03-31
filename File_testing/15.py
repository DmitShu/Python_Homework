myFile = open('File1.txt', 'rt', encoding='utf8')
print(myFile.readline())
myFile = open('File1.txt', 'rt', encoding='utf8')
print(myFile.readlines())
myFile = open('File1.txt', 'rt', encoding='utf8')
for line in myFile:
    print(line)

myFile2 = open('File2.txt', 'w', encoding='utf8')
myFile2.write('ttt')
print('zzz', file=myFile2)