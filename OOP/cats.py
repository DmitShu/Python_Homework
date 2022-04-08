import json
from cat import CatClass

#словарик кошечек
catsall = []

try:
    with open('pets.json', encoding='utf8') as f:
         tmpl = json.load(f)
except Exception as ex:
    print('Ошибка открытия файла')
    tmpl = []

for item, value in tmpl.items():
    if item == 'results':
        for it1 in value:
            if it1.get('species').get('code') == 'cat':
                catsall.append(CatClass(it1.get('name'), it1.get('gender').get('name'), it1.get('age')))

for cat in catsall:
    print(f'Имя котэ: "{cat.name}"\t Пол кашака: "{cat.gender}"\t Возраст кашака: "{cat.age}"')
