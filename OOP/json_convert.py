import json

with open('pets.json', encoding='utf8') as f:
    tmp = json.load(f)
print(tmp)

with open('pets.json', 'w', encoding='utf8') as f:
    json.dump(tmp, f, ensure_ascii=False, indent=4)

with open('pets.json', encoding='utf8') as f:
    print(f.read())