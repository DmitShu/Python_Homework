import requests
import lxml.html
from lxml import etree

# import lxml.html
#
# html = ''' <html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>
# '''
#
# tree = lxml.html.document_fromstring(html)
#
# text = tree.xpath('/html/body/tag1/tag2/text()')
#
# print(text)


# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python
#
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath(
#     '/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.
#
# print(title)  # выводим полученный заголовок страницы


# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python
#
#
# # создадим объект ElementTree. Он возвращается функцией parse()
#
# tree = lxml.html.document_fromstring(html)
# # tree = etree.parse('Welcome to Python.org.html',
# #                    lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера
#
# ul = tree.findall('body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath
#
# # создаём цикл в котором мы будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find('a')  # в каждом элементе находим где хранится название. У нас это тег <a>
#     time = li.find('time')
#     print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием

html = requests.get('https://www.yacgms.ru/fakticheskie-dannye/').content  # фактические данные


# создадим объект ElementTree. Он возвращается функцией parse()
tree = lxml.html.document_fromstring(html)

tbody = tree.findall('body/div[1]/div[2]/div/div/div[1]/main/article/div/div/table/tbody/tr')  # помещаем в аргумент методу findall скопированный xpath

print('Данные в реальном времени по ЯО \nМС - Метеорологическая станция \nАМС - Автоматическая метеорологическая станция')
print(69*'-')

for tr in tbody:
    tmp = tr.findall('td')
    if len(tmp):
        print(f'\t{tmp[0].text}\nТемпература: {tmp[1].text} °C\nДавление: {tmp[3].text} мм р.ст.\nВлажность: {tmp[4].text} %\nСкорость ветра: {tmp[2].text} м/с\n')