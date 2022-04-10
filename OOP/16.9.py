class Volunteer:
    def __init__(self, name='', surname='', city='', status=''):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def getInfo(self):
        return [self.name, self.surname, self.city, self.status]

#список гостей
allguests = []

#метод добавления гостей в список
def addguest():
    try:
        nb = int(input('Сколько гостей добавить: '))
        for i in range(nb):
            nm = input(f'Ведите имя гостя № {i + 1}: ')
            sm = input(f'Ведите фамилию гостя № {i + 1}: ')
            ct = input(f'Ведите город гостя № {i + 1}: ')
            ss = input(f'Ведите статус гостя № {i + 1}: ')
            allguests.append(Volunteer(nm, sm, ct, ss))
    except Exception as ex1:
        # print(ex1)
        print('Данные введены не верно.', ex1, 'Попробуйте снова.')
        addguest()

#метод извлечения гостей
def getguests():
    if allguests:
        print('Список гостей:')
        for guest in allguests:
            print(f'{allguests.index(guest)+1}'
                  f'. {guest.getInfo()[0]}'
                  f' {guest.getInfo()[1]}'
                  f', г.{guest.getInfo()[2]}'
                  f', статус:"{guest.getInfo()[3]}"')
    else:
        print('Список гостей пуст')

addguest()

print(96*'\/')

getguests()