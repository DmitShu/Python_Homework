# #Ввод чисел и сортировка
# num = int(input('Введите число:'))
# data=[]
# while num !=0:
#     data.append(num)
#     num = int(input('Введите число:'))
# data.sort()
# print(data)
# wrd = input('Введите:')
# data=[]
# while wrd != '':
#     if wrd not in data:
#         data.append(wrd)
#     wrd = input('Введите:')
# for it in data:
#     print(it)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print(69*'*')
print("Уважаемый клиент, вам доступны следующие условия:")
print()
for bnk, per in per_cent.items():
    print(f'Банк "{bnk}"\t Процент по вкладу: {per}')
print(69*'*')
mny = float(input('Введите сумму, которую вы планируете внести: '))
print('Что вы получите через год:')
for bnk, per in per_cent.items():
     print(f'Банк "{bnk}"\t Сумма на счету: {round((per/100+1)*mny, 2)}\t Ваш доход: {round(per*mny/100, 2)}')
print(69*'*')
print('Лучшие условия:')
print(69*'*')
# r = 0
# for k in per_cent:
#     if per_cent[k] > r:
#         r = per_cent[k]
#         m = k
# print('макс:', m, round(r * money / 100, 2))