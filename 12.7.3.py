#Ввод чисел и сортировка
num = int(input('Введите число:'))
data=[]
while num !=0:
    data.append(num)
    num = int(input('Введите число:'))
data.sort()
print(data)
wrd = input('Введите:')
data=[]
while wrd != '':
    if wrd not in data:
        data.append(wrd)
    wrd = input('Введите:')
for it in data:
    print(it)