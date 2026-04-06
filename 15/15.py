'''
import json
frage = int(input('у вас новый продукт?:'))
if frage == 'да' or frage == 'Да':
    neu_name = input('введите название продукта:')
    neu_price = input('введите цену продукта:')
    neu_available = input('введите есть ли он в наличии (True/False):')
    neu_weight = input('введите вес продукта:')
    
    new_product = {
    "name": neu_name,
    "price": neu_price,
    "available": neu_available,
    "weight": neu_weight
    }
    with open("json.txt", "r", encoding="utf-8") as f:
        data = json.load(f)
        data['products'].append(new_product)
    with open("json.txt", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        for products in data['products']:
            print(f'\nназвание продукта: {products["name"]}')
            print(f'цена продукта: {products["price"]}')
            print(f'вес продукта: {products["weight"]}')
            if products["available"] == True:
                print(f'В наличии')
            else:
                print(f'китай партия разочерован')
else:
    with open("json.txt", "r", encoding="utf-8") as f:
        data = json.load(f)
        for products in data['products']:
            print(f'\nназвание продукта: {products["name"]}')
            print(f'цена продукта: {products["price"]}')
            print(f'вес продукта: {products["weight"]}')
            if products["available"] == True:
                print(f'В наличии')
            else:
                print(f'китай партия разочерован')э
'''
with open('worterbuch.txt', encoding='utf-8') as f, open('worterbuch.txt',"w", encoding='utf-8') as wf:
    ru_er = {}
    for en_ru in f:
        if '-' in en_ru and worter[0] not in ru_er:
            worter = en_ru.split('-')
            wf.write(f'{worter[0]} - {worter[1]}')
        elif '=' in en_ru and worter[0] not in ru_er:
            worter = en_ru.split('=')
            ru_er[worter[0]] = worter[1]
            wf.write(f'{worter[0]} - {worter[1]}') 
        elif '–' in en_ru and worter[0] not in ru_er:
            worter = en_ru.split('–')
            ru_er[worter[0]] = worter[1]
            wf.write(f'{worter[0]} - {worter[1]}')
        else:
            print('китай партия забирает у вас миска рис')
            continue