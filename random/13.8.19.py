# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:
#
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
#
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
#
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.

#Setings:
low = 0.0         # стоимость до 18
avg = 990.0       # стоимость 18-25
hig = 1390.0      # стоимость после 25
dsc = 0.1         # скидка ( 0 - 1 )
pfd = 4           # билетов для скидки

try:
    tcst = 0.0
    print('Введите необходимое число билетов')
    tnm = int(input())
    if tnm < 1:
        raise ValueError("Мало билетов")
    elif tnm >= pfd:
        dsc = 1 - dsc
    else:
        dsc = 1
    while tnm:
        print(f'Промежуточная сумма: {tcst} \t Билетов зарегистрировать: {tnm}')
        print(f'Введите возраст посетителя:')
        age = int(input())
        if age < 18:
            tcst += low*dsc
        elif 18 <= age <= 25:
            tcst += avg*dsc
        else:
            tcst += hig*dsc
        tnm -= 1
    print(f'Итоговая сумма: {tcst}')
except:
    print("Чета пошло не так. Проверьте данные и попробуйте снова.")