import json
#
# with open('tmp.json', encoding='utf8') as f:
#     tmp = json.load(f)
# print(tmp)
#
# with open('tmpw.json', 'w', encoding='utf8') as f:
#     json.dump(tmp, f, ensure_ascii=False, indent=4)
#
# with open('tmpw.json', encoding='utf8') as f:
#     print(f.read())
itemslist = {'timestamp': 'int', 'referer': 'url', 'location': 'url', 'remoteHost': 'str', 'partyId': 'str',
          'sessionId': 'str', 'pageViewId': 'str', 'eventType': 'val', 'item_id': 'str', 'item_price': 'int',
          'item_url': 'url', 'basket_price': 'str', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool',
          'firstInSession': 'bool', 'userAgentName': 'str'}

Error = []
try:
    with open('real.json', encoding='utf8') as f:
         tmpl = json.load(f)
except Exception as ex:
    print('Ошибкв открытия файла', ex)


def CheckInt(item):
     return isinstance(item, int)


def CheckStr(item):
     return isinstance(item, str)


def CheckBool(item):
     return isinstance(item, bool)

def CheckUrl(item):
     if isinstance(item, str):
          return item.startswith('http://') or item.startswith('https://')
     else:
          return False

def CheckStrValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False

def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})

for items in tmpl:
    for item in items:
        if item in itemslist:
            if itemslist[item] == 'int':
                if not CheckInt(items[item]):
                    ErrorLog(item, items[item], f' ожидали тип {itemslist[item]}')
            elif itemslist[item] == 'str':
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], f' ожидали тип {itemslist[item]}')
            elif itemslist[item] == 'bool':
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], f' ожидали тип {itemslist[item]}')
            elif itemslist[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], f' ожидали тип {itemslist[item]}')
            elif itemslist[item] == 'val':
                if not CheckStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(item, items[item], ' ожидали itemBuyEvent или itemViewEvent')
            else:
                ErrorLog(item, items[item], 'неожиданное значение')
        else:
            ErrorLog(item, items[item], 'неизвестная переменная')

if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)