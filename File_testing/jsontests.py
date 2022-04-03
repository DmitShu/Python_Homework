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
items = {'timestamp': 'int', 'referer': 'url', 'location': 'url', 'remoteHost': 'str', 'partyId': 'str',
          'sessionId': 'str', 'pageViewId': 'str', 'eventType': 'val', 'item_id': 'str', 'item_price': 'int',
          'item_url': 'url', 'basket_price': 'str', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool',
          'firstInSession': 'bool', 'userAgentName': 'str'}


with open('real.json', encoding='utf8') as f:
     tmpl = json.load(f)


def CheckInt(item):
     return isinstance(item, int)


def CheckStr(item):
     return isinstance(item, str)


def CheckBool(item):
     return isinstance(item, bool)


def CheckUrl(item):
     if isinstance(item, str):
          return item.startswith('http:\\') or item.startswith('https:\\')
     else:
          return False
