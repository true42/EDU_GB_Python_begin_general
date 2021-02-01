#  проверяем типы объектов и выводим их в своём формате

any_type_list = [1, "3", True, [2, '5', 'word'], (22,'test', [1, 3, 'one']), {'1': 'one', '2':'two'}]
print(any_type_list)

def type_item(item, indent = ""):
    if type(item) == int:
        print(f'{indent} {item} - Это чиселки')
    elif type(item) == dict:
        print(f'{indent} {item} - Это словарик')
    elif type(item) == tuple:
        print(f'{indent} {item} - Это кортежик')
    elif type(item) == list:
        print(f'{indent} {item} - Это списочек')
    elif type(item) == bool:
        print(f'{indent} {item} - Это булечки')
    elif type(item) == str:
        print(f'{indent} {item} - Это буковки')

for item in any_type_list:
    type_item(item)
    try: # Проверяем итерируемость объекта, чтоб проверить объекты в нём
        iter(item)
        if len(item) > 1: #если объектов больше 1
            for in_item in item:
                type_item(in_item, '     ') # смотрим тип объекта внутри итерируемого объекта
    except TypeError:
        pass
