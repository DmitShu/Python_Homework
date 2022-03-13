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
for bnk, per in per_cent.items():
    print(f'Банк "{bnk}"\t Процент по вкладу: {per}')
print(69*'*')
print()
money = float(input('Введите сумму, которую вы планируете внести: '))
print()
print('Что вы получите через год:')
print()
deposit = []
for bnk, per in per_cent.items():
     dep = per*money/100
     print(f'Банк "{bnk}"\t Сумма на счету: {round((per/100+1)*money, 2)}\t Ваш доход: {round(dep, 2)}')
     deposit.append(dep)
print()
print('Лучшие условия:')

#print(f'Банк "{(max(per_cent, key=per_cent.get))}"\t Сумма на счету: {round((per / 100 + 1) * money, 2)}\t Ваш доход: {round(dep, 2)}')

print(69*'*')
print()
print("Техническая информация (как в задании было):")
print(f' money = {money}')
print(f' deposit = {deposit}')
print(f' Максимальная сумма, которую вы можете заработать — {max(deposit)}')
print(69*'*')